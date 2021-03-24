from match_manager.match_context import MatchContext
from typing import List
from telethon import events
from telethon.tl.custom.message import Message
from db_methods.group_match import GroupMatchJobs
from rps import RPS_CORE
from telethon.tl.custom.button import Button


match_contexts: List[MatchContext] = []


@events.register(
    events.NewMessage(
        incoming=True, func=lambda e: e.is_group, pattern='^/newmatch'))
async def new_match(event: Message):
    bot_username = 'rps2bot'
    with GroupMatchJobs() as gmj:
        unfinished = gmj.unfinished_match(event.chat_id)
        if unfinished:
            if RPS_CORE.GetMatch(unfinished.match_id):
                if not unfinished.started:
                    button = Button.url(
                        "Join",
                        "https://t.me/{}?start=join_{}_{}".format(
                            bot_username, event.chat_id, unfinished.match_id
                        )
                    )
                    await event.reply('_You are in Match!_', buttons=button)
                    return
            else:
                gmj.remove_match(unfinished)

        match_id = RPS_CORE.NewMatch
        gmj.add_match(match_id, event.chat_id, event.sender_id)
        button = Button.url(
            "Join",
            "https://t.me/{}?start=join_{}_{}".format(
                bot_username, event.chat_id, match_id
            )
        )
        await event.reply(' _Match created!_', buttons=button)


@events.register(
    events.NewMessage(
        incoming=True, func=lambda e: e.is_private, pattern='^/start join_'))
async def join_match(event: Message):
    splited = event.raw_text.split('=')[-1].split('_')
    group_id = int(splited[1])
    match_id = splited[2]
    with GroupMatchJobs() as gmj:
        group = gmj.get_match_secure(match_id, group_id)
        if group:
            if not group.finished and not group.started:
                match = RPS_CORE.GetMatch(group.match_id)
                if match:
                    if match.AddPlayer(event.sender_id):
                        await event.reply('*Joined!*')
                        await event.client.send_message(
                            group_id,
                            "[{}](tg://user?id={}) Joined!".format(
                                event.sender.first_name,
                                event.sender_id
                            )
                        )
                else:
                    gmj.remove_match(match_id)
            else:
                await event.reply('_Match is finished or started already!_')


@events.register(
    events.NewMessage(
        incoming=True, func=lambda e: e.is_group, pattern='^/startmatch'))
async def start_match(event: Message):
    global match_contexts

    splited = event.raw_text.split(' ')
    if len(splited) > 1:
        round_count = int(splited[1])
        if len(splited) > 2:
            round_duration = int(splited[2])
    else:
        round_count = 5
        round_duration = 30

    with GroupMatchJobs() as gmj:
        match = gmj.unfinished_match(event.chat_id)
        if match:
            if not match.started:
                if RPS_CORE.GetMatch(match.match_id):
                    context = MatchContext(
                        event.client,
                        event.chat_id,
                        match.match_id,
                        round_duration=round_duration,
                        round_count=round_count
                    )
                    match_contexts.append(context)
                    context.start()
                    gmj.started(match)
                    await event.reply(
                        'Match Started!\n\n'
                        + '_Total round_: `{}`, _Round timeout_: `{}`'.format(
                            round_count,
                            round_duration
                        )
                    )
                else:
                    gmj.remove_match(match)
                    await event.reply(
                        'No match found\n_Start a new match with /newmatch._')
                    return
            else:
                await event.reply('Match already started!!')
        else:
            await event.reply(
                'No match found\n_Start a new match with /newmatch._')


@events.register(
    events.CallbackQuery(pattern="^choisCard_")
)
async def card_choosed(event):
    global match_contexts

    splited = str(event.data).split('_')
    match_id = splited[1]
    card = splited[2].replace("'", "")

    match_context = [x for x in match_contexts if x.match_id == match_id][0]
    if match_context:
        if match_context.card_selected(event.sender.id, card):
            await event.answer("Selected!")
            await event.edit(f"_{card}_ Selected!")

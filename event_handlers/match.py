from telethon import events
from telethon.tl.custom.message import Message
from db_methods.group_match import GroupMatchJobs
from rps import RPS_CORE
from telethon.tl.custom.button import Button


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
                    await event.reply('You are in Match!', buttons=button)
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
        await event.reply('Match created!', buttons=button)

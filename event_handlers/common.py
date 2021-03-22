# event-handlers/common.py
# for common hanlers like /start /help & ...
from telethon import events
from db_methods.users import UsersJobs
from telethon.tl.custom.message import Message
from telethon.tl.types import User


@events.register(
    events.NewMessage(pattern='^/start$', func=lambda e: e.is_private))
async def start_message(event: Message):
    await event.respond('Hey there!')
    with UsersJobs() as uj:
        user = uj.get_user(event.sender_id)
        sender: User = event.sender
        if user:
            if user.username != sender.username:
                uj.update(
                    user, sender.first_name, sender.username, sender.lang_code)
                await event.respond('Updated!')
        else:
            uj.insert_user(
                sender.id,
                sender.first_name,
                sender.username,
                sender.lang_code)
            await event.respond('Inserted')

# event-handlers/common.py
# for common hanlers like /start /help & ...
from telethon import events

@events.register(events.NewMessage(pattern= '^/start$', func=lambda e: e.is_private))
async def start_message(event):
    await event.respond('Hey there!')
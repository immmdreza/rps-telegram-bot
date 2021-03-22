from telethon import TelegramClient
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


def main():
    from dotenv import load_dotenv
    # loading from .env (see .env.example)
    load_dotenv()

    import os
    # Use your own values from my.telegram.org
    api_id = os.getenv('API_ID')
    api_hash = os.getenv('API_HASH')
    # your bot token
    bot_token = os.getenv('BOT_TOKEN')

    print(":: Starting the bot ::")
    # We have to manually call "start" if we want an explicit bot token
    bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)

    print(":: Setting up event handlers ::")
    from event_handlers import handlers
    # all handles should be stored in event_handler folder
    # then appened to handlers list in __init__.py
    added_handler = 0
    for handler in handlers:
        print(f"╚ :: Added '{handler.__name__}' ::")
        bot.add_event_handler(handler)
        added_handler += 1

    if added_handler == 0:
        print("╚ :: No handler added!! ::")

    print(":: Running forever!! ::")
    bot.run_until_disconnected()


if __name__ == '__main__':
    main()

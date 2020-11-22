import os
from dotenv import load_dotenv
from telethon import TelegramClient, events

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
APP_API_ID = os.getenv('APP_API_ID')
APP_API_HASH = os.getenv('APP_API_HASH')

bot = TelegramClient('bot', APP_API_ID, APP_API_HASH).start(bot_token=BOT_TOKEN)

@bot.on(events.NewMessage(pattern='/start'))
async def start(event):
    """Send a message wnen the command /start is issued"""
    me = await bot.get_me()
    print(me.stringify())

    await event.respond('Hi! I am bot-popugai, just repeat your messages. me: {}'.format(me.username))
    # await bot.send_message(-1817059, 'Hello, myself!')
    raise events.StopPropagation

@bot.on(events.NewMessage)
async def echo(event):
    """Echo the user message"""
    await event.respond(event.text)

def main():
    """
    Start the bot
    """
    bot.run_until_disconnected()

if __name__ == "__main__":
    main()

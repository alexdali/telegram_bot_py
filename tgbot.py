import requests
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
TG_CHAT_ID = os.getenv('TG_CHAT_ID')

def send_msg(text, chat_id):
  """
  function send message from bot to telegram chat
  """

  params = {
    'text': text,
    'chat_id': chat_id,
  }

  response = requests.get('https://api.telegram.org/bot{}/sendMessage'.format(BOT_TOKEN), params=params)

  print(response)


if __name__ == "__main__":
    send_msg('Hi, just test!!!', TG_CHAT_ID)
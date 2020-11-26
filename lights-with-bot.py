!pip install adafruit-io
import os

x = os.getenv('ADAFRUIT_IO_USERNAME')
y = os.getenv('ADAFRUIT_IO_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

from Adafruit_IO import Client, Feed
aio = Client(x,y)
feed = Feed(name='bot')
result = aio.create_feed(feed)

from Adafruit_IO import Data
!pip install python-telegram-bot

from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

def start(update,context):
    print(str( update.effective_chat.id ))
    context.bot.send_message(chat_id = update.effective_chat.id,text="Welcome! Type 'Turn on the light' or /on to switch on the light bulb. Type 'Turn off the light' or /off to switch off the light bulb.")

def unknown(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SORRY! INVALID! TYPE AGAIN PLEASE")

def on(update,context):
  context.bot.send_message(chat_id=update.effective_chat.id,text="Light has been turned on!")
  context.bot.send_photo(chat_id=update.effective_chat.id, photo= "https://blog.spiritualify.com/wp-content/uploads/2019/10/What-Is-the-Spiritual-Meaning-of-the-Lights-that-Turn-On-and-Off-by-Themselves.jpg")
  value = Data(value=1)
  value_send = aio.create_data('bot', value)

def off(update,context):
  context.bot.send_message(chat_id=update.effective_chat.id,text="Light has been turned off!")
  context.bot.send_photo(chat_id=update.effective_chat.id, photo= "https://previews.123rf.com/images/colinbehrens/colinbehrens1810/colinbehrens181000005/110239291-light-bulb-black-background-turned-off.jpg")
  value = Data(value=0)
  value_send = aio.create_data('bot', value)

u = Updater(''TELEGRAM_TOKEN',use_context = True')
dp = u.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
dp.add_handler(CommandHandler('start', start))
dp.add_handler(MessageHandler(Filters.command, unknown))
dp.add_handler(MessageHandler(Filters.text, given_message))

u.start_polling()
u.idle()

import telebot
from telebot import types
from telebot.types import LabeledPrice

bot = telebot.TeleBot("7427769894:AAH4QSYVWyIEm112Gf1gAytJ81W8kmCsg5o", parse_mode=None)

smallSpinPrice = [LabeledPrice(label='Small Spin', amount=100)]
bigSpinPrice = [LabeledPrice(label='Big Spin', amount=200)]

startwebBtn = types.InlineKeyboardButton('Start Now', callback_data='started')
joincBtn = types.InlineKeyboardButton('Join Our Channel!', url='https://t.me/+IrvQZoV91IVkYzU1')
joingBtn = types.InlineKeyboardButton('Join Our Chat Group!', url='https://t.me/+WdGn-u4HNbsyOTc1')

startmenu = types.InlineKeyboardMarkup()
startmenu.add(startwebBtn)
startmenu.add(joincBtn)
startmenu.add(joingBtn)

wallet = types.InlineKeyboardButton('Wallet', callback_data='wallet')
startSpin = types.InlineKeyboardButton('Launch Spin App', url='https://t.me/dev_spin_bot/spinwebapp')

spinSelection = types.InlineKeyboardMarkup()
spinSelection.add(wallet)
spinSelection.add(startSpin)


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Welcome to SpinteleBot!", reply_markup=startmenu)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'started':
        bot.send_message(call.message.chat.id, "Choose your option", reply_markup=spinSelection)
    elif call.data == 'wallet':
        bot.send_message(call.message.chat.id, "Wallet : Under Dev")


print("Online")
bot.infinity_polling()

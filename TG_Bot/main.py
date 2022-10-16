import telebot

from telebot import types
TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name}!'
    bot.send_message(message.chat.id, mess, parse_mode='html')


#@bot.message_handler()
#def get_user_text(message):
#    if message.text == 'Hello':
#        bot.send_message(message.chat.id, 'И тебе привет!', parse_mode='html')
#    elif message.text == 'id':
#        bot.send_message(message.chat.id, f'Твой ID:{message.from_user.id}', parse_mode='html')
#    else:
#        bot.send_message(message.chat.id, 'Я тебя не понимаю!', parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Посетить сайт',url='https://www.google.ru'))
    bot.send_message(message.chat.id, 'Иди в гугл', reply_markup=markup)


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    website = types.KeyboardButton('Сайт')
    start = types.KeyboardButton('start')
    markup.add(website, start)
    bot.send_message(message.chat.id, 'Иди в гугл', reply_markup=markup)


bot.polling(none_stop=True)

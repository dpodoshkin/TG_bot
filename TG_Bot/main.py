import telebot

from telebot import types
TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Гороскоп на сегодня')
    btn2 = types.KeyboardButton('Гороскоп на месяц')
    markup.add(btn1,btn2)
    mess = f'Привет, {message.from_user.first_name}!'
    bot.send_message(message.chat.id, mess, parse_mode='html',reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == 'гороскоп на сегодня':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=6)
        btn1 = types.KeyboardButton('Овен (Aries)')
        btn2 = types.KeyboardButton('Телец (Taurus)')
        btn3 = types.KeyboardButton('Близнецы (Gemini)')
        btn4 = types.KeyboardButton('Рак (Cancer)')
        btn5 = types.KeyboardButton('Лев (Leo)')
        btn6 = types.KeyboardButton('Дева (Virgo)')
        btn7 = types.KeyboardButton('Весы (Libra)')
        btn8 = types.KeyboardButton('Скорпион (Scorpio)')
        btn9 = types.KeyboardButton('Стрелец (Sagittarius)')
        btn10 = types.KeyboardButton('Козерог (Capricorn)')
        btn11 = types.KeyboardButton('Водолей (Aquarius)')
        btn12 = types.KeyboardButton('Рыбы (Pisces)')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
        final_mess = 'Выдаю гороскоп на сегодня'

    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=6)
        btn1 = types.KeyboardButton('Овен (Aries)')
        btn2 = types.KeyboardButton('Телец (Taurus)')
        btn3 = types.KeyboardButton('Близнецы (Gemini)')
        btn4 = types.KeyboardButton('Рак (Cancer)')
        btn5 = types.KeyboardButton('Лев (Leo)')
        btn6 = types.KeyboardButton('Дева (Virgo)')
        btn7 = types.KeyboardButton('Весы (Libra)')
        btn8 = types.KeyboardButton('Скорпион (Scorpio)')
        btn9 = types.KeyboardButton('Стрелец (Sagittarius)')
        btn10 = types.KeyboardButton('Козерог (Capricorn)')
        btn11 = types.KeyboardButton('Водолей (Aquarius)')
        btn12 = types.KeyboardButton('Рыбы (Pisces)')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
        final_mess = 'Не понимаю'
    bot.send_message(message.chat.id, final_mess, parse_mode='html', reply_markup=markup)

# @bot.message_handler(commands=['website'])
# def website(message):
#     markup = types.InlineKeyboardMarkup()
#     markup.add(types.InlineKeyboardButton('Посетить сайт', url='https://www.google.ru'))
#     bot.send_message(message.chat.id, 'Открывай ссылку', parse_mode='html', reply_markup=markup)
#
#
# @bot.message_handler(commands=['help'])
# def website(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     website = types.KeyboardButton('/website')
#     start = types.KeyboardButton('/start')
#     markup.add(website, start)
#     bot.send_message(message.chat.id, 'Иди в гугл', reply_markup=markup)


bot.polling(none_stop=True)

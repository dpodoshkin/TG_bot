import telebot
from telebot import types
import requests
from bs4 import BeautifulSoup

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Овен')
    btn2 = types.KeyboardButton('Телец')
    btn3 = types.KeyboardButton('Близнецы')
    btn4 = types.KeyboardButton('Рак')
    btn5 = types.KeyboardButton('Лев')
    btn6 = types.KeyboardButton('Дева')
    btn7 = types.KeyboardButton('Весы')
    btn8 = types.KeyboardButton('Скорпион')
    btn9 = types.KeyboardButton('Стрелец')
    btn10 = types.KeyboardButton('Козерог')
    btn11 = types.KeyboardButton('Водолей')
    btn12 = types.KeyboardButton('Рыбы')
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
    bot.send_message(chat_id, f'Привет, {first_name}!\n'
                     'Выбери свой знак зодиака', parse_mode='html',reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_mess(message):
    chat_id = message.chat.id
    if message.chat.type == 'private':
        if message.text == 'Овен':
            url = 'https://7days.ru/astro/horoscope/aries/today'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='horoscope-7days')
            prophecy = section.find('div', class_='horoscope-7days__content_text').get_text(strip=True)
            bot.send_message(chat_id, prophecy)

        if message.text == 'Телец':
            url = 'https://7days.ru/astro/horoscope/taurus/today'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='horoscope-7days')
            prophecy = section.find('div', class_='horoscope-7days__content_text').get_text(strip=True)
            bot.send_message(chat_id, prophecy)

        if message.text == 'Близнецы':
            url = 'https://7days.ru/astro/horoscope/gemini/today'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='horoscope-7days')
            prophecy = section.find('div', class_='horoscope-7days__content_text').get_text(strip=True)
            bot.send_message(chat_id, prophecy)

        if message.text == 'Рак':
            url = 'https://7days.ru/astro/horoscope/cancer/today'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='horoscope-7days')
            prophecy = section.find('div', class_='horoscope-7days__content_text').get_text(strip=True)
            bot.send_message(chat_id, prophecy)

        if message.text == 'Лев':
            url = 'https://7days.ru/astro/horoscope/leo/today'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='horoscope-7days')
            prophecy = section.find('div', class_='horoscope-7days__content_text').get_text(strip=True)
            bot.send_message(chat_id, prophecy)

        if message.text == 'Дева':
            url = 'https://7days.ru/astro/horoscope/virgo/today'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='horoscope-7days')
            prophecy = section.find('div', class_='horoscope-7days__content_text').get_text(strip=True)
            bot.send_message(chat_id, prophecy)

        if message.text == 'Весы':
            url = 'https://7days.ru/astro/horoscope/libra/today'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='horoscope-7days')
            prophecy = section.find('div', class_='horoscope-7days__content_text').get_text(strip=True)
            bot.send_message(chat_id, prophecy)

        if message.text == 'Скорпион':
            url = 'https://7days.ru/astro/horoscope/scorpio/today'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='horoscope-7days')
            prophecy = section.find('div', class_='horoscope-7days__content_text').get_text(strip=True)
            bot.send_message(chat_id, prophecy)

        if message.text == 'Стрелец':
            url = 'https://7days.ru/astro/horoscope/sagittarius/today'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='horoscope-7days')
            prophecy = section.find('div', class_='horoscope-7days__content_text').get_text(strip=True)
            bot.send_message(chat_id, prophecy)

        if message.text == 'Козерог':
            url = 'https://7days.ru/astro/horoscope/capricorn/today'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='horoscope-7days')
            prophecy = section.find('div', class_='horoscope-7days__content_text').get_text(strip=True)
            bot.send_message(chat_id, prophecy)

        if message.text == 'Водолей':
            url = 'https://7days.ru/astro/horoscope/aquarius/today'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='horoscope-7days')
            prophecy = section.find('div', class_='horoscope-7days__content_text').get_text(strip=True)
            bot.send_message(chat_id, prophecy)

        if message.text == 'Рыбы':
            url = 'https://7days.ru/astro/horoscope/pisces/today'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            section = soup.find('div', class_='horoscope-7days')
            prophecy = section.find('div', class_='horoscope-7days__content_text').get_text(strip=True)
            bot.send_message(chat_id, prophecy)



bot.polling(none_stop=True)

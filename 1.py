import telebot

bot = telebot.TeleBot('token.emv')
from telebot import types

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Здесь вы можете купальники COD!", reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def get_text_messages(message):
        if message.text == '👋 Поздороваться':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
            btn1 = types.KeyboardButton('О нас')
            btn2 = types.KeyboardButton('Каталог')
            btn3 = types.KeyboardButton('Оплата и доставка')
            markup.add(btn1, btn2, btn3)

        elif message.text == 'О нас':
            bot.send_message(message.from_user.id,
                             'Мы произодство купальников премимум класса родом из Санкт-Петербурга, купальники изготовлены из двухслойного бифлекса, для обеспечения высочайшего качества на рынке',
                             parse_mode='Markdown')

        elif message.text == 'Каталог':
            bot.send_message(message.from_user.id,
                             'Выберите модель',
                             parse_mode='Markdown')

        elif message.text == 'Оплата и доставка':
            bot.send_message(message.from_user.id,
                             'Оплата осуществляется посредством платежной системы Юкасса в данном боте. Доставка курьером по СПБ',
                             parse_mode='Markdown')



bot.polling(none_stop=True, interval=0)
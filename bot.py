#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
import config
from fusionai import Text2ImageAPI


API_TOKEN = config.telebot_API_TOKEN

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
PLACEHOLDER
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def fusion_ai(message):
    bot.reply_to(message, 'Генерирую картинку...')
    Text2ImageAPI.generate_img(message.text)
    photo = open('decoded_image.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)


bot.infinity_polling()
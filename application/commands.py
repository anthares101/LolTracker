# coding=utf-8
import requests
from telebot import util

from application import bot, RIOT_KEY


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(commands=['summoner'])
def summoner(message):
    name = util.extract_arguments(message.text)

    if not name:
        bot.reply_to(message, "Especifique un nombre de invocador")
    else:
        r = requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+name+'?api_key=' + RIOT_KEY)
        if(r.status_code in range(200,299)):#Request accepted
            content = r.json()
            bot.reply_to(message, content["name"])
        else:#Request error
            bot.reply_to(message, "Invocador desconocido")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    """
    Hace un 'eco' de lo que se recibe y no se ha procesado en algún comando anterior.
    :param message:
    :return:
    """
    bot.reply_to(message, message.text)

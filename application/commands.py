# coding=utf-8
import requests
from telebot import util
from model.chat import Chat

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
        cid = chat_id = message.chat.id
        region = Chat.get_config(cid, "region").value
        url = 'https://'+region+'.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+name
        params = {
            'api_key': RIOT_KEY
        }
        r = requests.get(url, params)

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

# coding=utf-8
import requests

from application import bot


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(commands=['summoner'])
def summoner(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

    r = requests.get('https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/anthares101?api_key=' + RIOT_KEY)
    content = r.json()

    bot.reply_to(message, content["name"])


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    """
    Hace un 'eco' de lo que se recibe y no se ha procesado en algún comando anterior.
    :param message:
    :return:
    """
    bot.reply_to(message, message.text)

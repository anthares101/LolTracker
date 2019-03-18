# coding=utf-8
from application import bot, RIOT_KEY
import requests
import json


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(commands=['rotation'])
def rotation(message):
    response = requests.get("https://euw1.api.riotgames.com/lol/platform/v3/champion-rotations?api_key=" + RIOT_KEY)
    content = response.json()
    champs = ""
    with open('champion.json') as json_file:
        file = json.load(json_file)
        champion_list = file['data']
        for item in content["freeChampionIds"]:
            for champion_name in champion_list.keys():
                if champion_list[champion_name]['key'] == str(item):
                    champs += champion_list[champion_name]['name']
                    champs += '\n'

    bot.reply_to(message, champs)

@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    """
    Hace un 'eco' de lo que se recibe y no se ha procesado en algún comando anterior.
    :param message:
    :return:
    """
    bot.reply_to(message, message.text)

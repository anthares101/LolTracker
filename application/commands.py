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
        bot.send_message(message.chat.id, "Especifique un nombre de invocador")
    else:
        cid = chat_id = message.chat.id
        region = Chat.get_config(cid, "region")

        if region is None:
            bot.send_message(message.chat.id, "Utiliza /region para seleccionar una region primero")
        else:
            url = 'https://'+region.value+'.api.riotgames.com/lol/summoner/v4/summoners/by-name/'+name
            params = {
                'api_key': RIOT_KEY
            }
            r = requests.get(url, params)

            if(r.status_code in range(200,299)):#Request accepted
                content = r.json()
                summonerId= content["id"]

                url = 'https://' + region.value + '.api.riotgames.com/lol/league/v4/positions/by-summoner/' + summonerId
                r = requests.get(url, params)
                contentLeague = r.json()

                text = "*Nombre:* " + str(content["name"]) + "\n*Nivel:* " + str(content["summonerLevel"]) + "\n"
                text += "*SoloQ:* " + contentLeague[0]["tier"] + " " + contentLeague[0]["rank"] + " -> " + str(contentLeague[0]["leaguePoints"]) + " LP\n"
                text += "             Victorias: " + str(contentLeague[0]["wins"]) + "\n"
                text += "             Derrotas: " + str(contentLeague[0]["losses"]) + "\n"


                bot.send_message(message.chat.id, text, parse_mode="Markdown")

                #photo = open("Data/profileicon/" + content["profileIconId"] + ".png")
                #bot.send_photo(message.chat.id, photo)
            else:#Request error
                bot.send_message(message.chat.id, "Invocador desconocido")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    """
    Hace un 'eco' de lo que se recibe y no se ha procesado en algún comando anterior.
    :param message:
    :return:
    """
    bot.reply_to(message, message.text)

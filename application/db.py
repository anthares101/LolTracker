# coding=utf-8
from telebot import util
from application import bot
from model.chat import Chat
from application.boards import *


@bot.message_handler(commands=['save'])
def save(message):
    """
    Guarda un dato en el chat que se puede recuperar después
    """

    data = util.extract_arguments(message.text)
    if not data:
        bot.reply_to(message, "Debe indicar el dato que quiere que guarde")
        return

    chat_id = message.chat.id
    Chat.set_config(chat_id, 'memory', data)
    bot.reply_to(message, "Dato guardado. Usa /load para recuperar")


@bot.message_handler(commands=['load'])
def load(message):
    """
    Recupera un dato guardado con save
    """

    chat_id = message.chat.id
    data = Chat.get_config(chat_id, 'memory')
    if not data:
        bot.reply_to(message, "Aún no has guardado nada")
        return

    bot.reply_to(message, "Dato recuperado: %s" % data.value)

@bot.message_handler(commands=['region'])
def region(message):
    uid = message.chat.id
    data = Chat.get_config(uid, "region")
    if data is not None:
        bot.reply_to(message, "%s actualmente seleccionada" %data.value)
    region_board(message)


@bot.callback_query_handler(func=lambda lib: lib.data in ["br1","eun1","euw1","jp1","kr","la1","la2","na1","oc1","tr1","ru","pbe1"])
def set_region(lib):
    uid = lib.message.chat.id
    Chat.set_config(uid, "region", lib.data)
    bot.reply_to(lib.message, "%s seleccionada" %lib.data)



    #"br", "eune", "euw", "jp", "kr", "lan", "las", "na", "oce", "tr", "ru", "pbe"
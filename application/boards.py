from telebot import types
from application import bot


def region_board(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    keyboard.add(types.InlineKeyboardButton("br", callback_data="b1"),
                 types.InlineKeyboardButton("eune", callback_data="eun1"),
                 types.InlineKeyboardButton("euw", callback_data="euw1"),
                 types.InlineKeyboardButton("pj", callback_data="jp1"),
                 types.InlineKeyboardButton("kr", callback_data="kr"),
                 types.InlineKeyboardButton("lan", callback_data="la1"),
                 types.InlineKeyboardButton("las", callback_data="la2"),
                 types.InlineKeyboardButton("na", callback_data="na1"),
                 types.InlineKeyboardButton("oce", callback_data="oc1"),
                 types.InlineKeyboardButton("tr", callback_data="tr1"),
                 types.InlineKeyboardButton("ru", callback_data="ru"),
                 types.InlineKeyboardButton("pbe", callback_data="pbe1"),
    )

    bot.send_message(message.chat.id, "¿en que región estás?", reply_markup=keyboard)
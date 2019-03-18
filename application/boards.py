from telebot import types
from application import bot


def region_board(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    keyboard.add(types.InlineKeyboardButton("br", callback_data="br"),
                 types.InlineKeyboardButton("eune", callback_data="eune"),
                 types.InlineKeyboardButton("euw", callback_data="euw"),
                 types.InlineKeyboardButton("pj", callback_data="jp"),
                 types.InlineKeyboardButton("kr", callback_data="kr"),
                 types.InlineKeyboardButton("lan", callback_data="lan"),
                 types.InlineKeyboardButton("las", callback_data="las"),
                 types.InlineKeyboardButton("na", callback_data="na"),
                 types.InlineKeyboardButton("oce", callback_data="oce"),
                 types.InlineKeyboardButton("tr", callback_data="tr"),
                 types.InlineKeyboardButton("ru", callback_data="ru"),
                 types.InlineKeyboardButton("pbe", callback_data="pbe"),
    )

    bot.send_message(message.chat.id, "¿en que región estás?", reply_markup=keyboard)
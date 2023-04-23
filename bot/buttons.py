# -----------------------------------------------------------
# Import modules
# -----------------------------------------------------------
# API Telegram bot
from telebot import types
# -----------------------------------------------------------
# Codes other files project
# -----------------------------------------------------------
# text for buttons
from data.buttons.names import buttons_name_dict


def main():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(buttons_name_dict["Enter sentences"])
    item2 = types.KeyboardButton(buttons_name_dict["Grammar"])
    markup.add(item1, item2)
    return markup
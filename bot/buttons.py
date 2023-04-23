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


def get_current_button(buttons_reply_markup):
    """
    :param buttons_reply_markup: It's types.ReplyKeyboardMarkup(resize_keyboard=True)
    :return: string that it is list of names of buttons
    """
    result = str()
    for x in buttons_reply_markup.keyboard[0]:
        for value in x.values():
            result = result + value + ", "
    return result[0:-2]

def main():
    """
    :return: main button
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(buttons_name_dict["Enter sentences"])
    item2 = types.KeyboardButton(buttons_name_dict["Grammar"])
    markup.add(item1, item2)
    return markup

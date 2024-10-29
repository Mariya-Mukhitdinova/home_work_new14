from telebot import types

def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text="UZS_USD")
    button2 = types.KeyboardButton(text="USD_UZS")

    kb.add(button1)
    kb.add(button2)
    return kb
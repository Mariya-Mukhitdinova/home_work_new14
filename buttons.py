from telebot import types

def main_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(text="RUB")
    button2 = types.KeyboardButton(text="USD")
    button3 = types.KeyboardButton(text="EVRO")

    kb.add(button1)
    kb.add(button2)
    kb.add(button3)
    return kb
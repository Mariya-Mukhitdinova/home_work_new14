import telebot
import buttons

bot = telebot.TeleBot(token = "7551169428:AAHtv4aXVn90FpysBZn78TjWUEwl1nnM51w")

@bot.message_handler(commands=["start"])
def start(message):
    user_id = message.from_user.id
    bot.send_message(user_id, f"Вас приветствует обмен валют!")
    bot.send_message(user_id, "Введите своё имя!")
    print(user_id)
    bot.register_next_step_handler(message, get_name)
def get_name(message):
    user_id = message.from_user.id
    name = message.text
    bot.send_message(user_id, "Выберите действие!", reply_markup=buttons.main_menu())
    bot.register_next_step_handler(message, change, name)
def change(message, name):
    user_id = message.from_user.id
    if message.text == "UZS_USD":
        bot.send_message(user_id, "Введите сумму: ")
        bot.register_next_step_handler(message, change_uzs)
    elif message.text == "USD_UZS":
        bot.send_message(user_id, "Введите сумму: ")
        bot.register_next_step_handler(message, change_usd)
def change_uzs(message):
    user_id = message.from_user.id
    uzs = float(message.text)
    result = uzs // 12600
    bot.send_message(user_id, f"{uzs} сум = {result}$")

def change_usd(message):
    user_id = message.from_user.id
    usd = float(message.text)
    result = usd * 12600
    bot.send_message(user_id, f"{usd}$ = {result}сум")







bot.infinity_polling()
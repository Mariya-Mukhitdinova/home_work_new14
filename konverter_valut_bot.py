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
    bot.register_next_step_handler(message, change)
def change(message):
    user_id = message.from_user.id
    if message.text == "RUB":
        bot.send_message(user_id, "Введите сумму: ")
        bot.register_next_step_handler(message,change_ru)
    elif message.text == "USD":
        bot.send_message(user_id, "Введите сумму: ")
        bot.register_next_step_handler(message, change_usd)
    elif message.text == "EVRO":
        bot.send_message(user_id, "Введите сумму: ")
        bot.register_next_step_handler(message, change_evro)

def change_ru(message):
    user_id = message.from_user.id
    uzs = float(message.text)
    result = uzs // 131
    bot.send_message(user_id, f"{result} рублей")
    bot.send_message(user_id, f"Выберите действие:", reply_markup=buttons.main_menu())
    bot.register_next_step_handler(message, change)

def change_usd(message):
    user_id = message.from_user.id
    uzs = float(message.text)
    result = uzs // 12600
    bot.send_message(user_id, f"{result} долларов")
    bot.send_message(user_id, f"Выберите действие:", reply_markup=buttons.main_menu())
    bot.register_next_step_handler(message, change)
def change_evro(message):
    user_id = message.from_user.id
    uzs = float(message.text)
    result = uzs // 13807
    bot.send_message(user_id, f"{result} евро")
    bot.send_message(user_id, f"Выберите действие:", reply_markup=buttons.main_menu())
    bot.register_next_step_handler(message, change)

bot.infinity_polling()
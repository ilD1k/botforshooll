import telebot
from config import token

bot = telebot.TeleBot(token)


@bot.message_handler(commands=["start"])
def start(message):
    name = message.chat.first_name
    bot.send_message(message.chat.id, f'Привет! {name}.\n')
    bot.send_message(message.chat.id, "это новый бот квестик by ilD1k")
    bot.send_message(message.chat.id, "Твой первый вопрос"
                                      " Ты хочешь посуетить но как??"
                                      " 1) дотка"
                                      " 2) школа"
                                      " 3) гулять")

    bot.register_next_step_handler(message, user_answer)


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Все сломал?? Вызывай старшего")
    bot.send_message(message.chat.id, 'Свяжись с [создателем](https://t.me/ildics)',

                     parse_mode='Markdown', )


@bot.message_handler(content_types=["text"])
def proverka(message):
    bot.send_message(message.chat.id, "Я такого не знаю")


def user_answer(message):
    if message.text == "1":
        bot.send_message(message.chat.id, "ты выйграл катку"
                                          " У тебя выбор"
                                          " 1) на седня хватит"
                                          " 2) регну еще ")

        with open("team2.jpg", "rb") as photo:
            bot.send_photo(message.chat.id, photo)

        bot.register_next_step_handler(message, vibor_dota)

    elif message.text == "2":
        bot.send_message(message.chat.id, "ты че???"
                                          " Квестик - провален")

        with open("f.png", "rb") as f:
            bot.send_photo(message.chat.id, f)

        bot.register_next_step_handler(message, start)


    elif message.text == "3":
        bot.send_message(message.chat.id, "Ты оч успешно пошел гулять"
                                          " Выбор "
                                          " 1) Ну че домой пойду доту регну"
                                          " 2) Пойду к моему bro")

        with open("gulaem.png", "rb") as gulaem:
            bot.send_photo(message.chat.id, gulaem)

        bot.register_next_step_handler(message, vibor)


def vibor_dota(message):
    if message.text == "1":
        bot.send_message(message.chat.id, "Квест пройден - ПОБЕДА")

        with open("team.jpg", "rb") as team:
            bot.send_photo(message.chat.id, team)

        bot.register_next_step_handler(message, start)

    elif message.text == "2":
        bot.send_message(message.chat.id, "Ты слил 100 ммр "
                                          " Квест пройден - ПОРАЖЕНИЕ")

        with open("dyrak.jpg", "rb") as dyrak:
            bot.send_photo(message.chat.id, dyrak)

        bot.register_next_step_handler(message, start)

    else:
        bot.send_message(message.chat.id, "ты чет не то написал")

        bot.register_next_step_handler(message, start)


def vibor(message):
    if message.text == "1":
        bot.send_message(message.chat.id("Ты пришел домой и регнул доту"
                                         " Квест пройден - ПОБЕДА"))

        with open("sigma.jpg", "rb") as sigma:
            bot.send_photo(message.chat.id, sigma)

        bot.register_next_step_handler(message, start)

    if message.text == "2":
        bot.send_message(message.chat.id, "Ты успешно сходил к bro"
                                          " Квест пройден - ПОБЕДА")
        with open("sigma3.jpg", "rb") as xd:
            bot.send_photo(message.chat.id, xd)

        bot.register_next_step_handler(message, start)

    else:
        bot.send_message(message.chat.id, "ты чет не то написал")
        bot.register_next_step_handler(message, start)


bot.polling()

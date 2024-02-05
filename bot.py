import telebot
from telebot.types import Message
from config import token
from jso4k import write_to_file, read_from_db
from random import choice


phrases = ["Уффффф чо за гипер стикер пупсик", "Эта типа малеф до травмы в 1999?", "Топ топ ножками в школу рабы системы",
           "пон", "Поньк", "мегапон", "харош", "сигма", "не будь дурак саси кулак стэтхем"]



def update_user_data():
    return read_from_db()


user_data = update_user_data()

bot = telebot.TeleBot(token)



@bot.message_handler(commands=["start"])
def start(message: Message):
    name = message.chat.first_name
    bot.send_message(message.chat.id, f'Привет! {name}.\n')
    bot.send_message(message.chat.id, "бот рассылает расписание уроков для 7 д класса")
    user_data[message.chat.id] = message.chat.id
    write_to_file(user_data)


@bot.message_handler(commands=["admin"], func=lambda message: message.from_user.id == 5085094693)
def admin(message):
    bot.send_message(message.chat.id, "Ку илюх"
                                      " Кидай расписание")
    bot.register_next_step_handler(message, send_raspisane)


def send_raspisane(message):
    user_data = update_user_data()
    for chat_id in user_data:
        try:
            bot.send_message(chat_id, message.text)
        except Exception as e:
            print(e, "сломали бота")


@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Все сломал или нашел не дочёты?")
    bot.send_message(message.chat.id, 'Свяжись с [создателем](https://t.me/ildics)',
                     parse_mode='Markdown', )
    write_to_file(user_data)

@bot.message_handler(content_types=["text"], func=lambda message: message.from_user.id == 236725960)
def kirill(message):
    bot.send_message(message.chat.id, "Привет кирюх твое сообщение уже было отправлено Илье")
    bot.forward_message(5085094693, message.chat.id, message.id)
    write_to_file(user_data)


@bot.message_handler(content_types=["text"], func=lambda message: message.text == "дурачье")
def dyrachyo(message):
    bot.send_message(message.chat.id, "Да как ты нашел эту фичу??")
    with open("./da.png", "rb") as photo:
        bot.send_photo(message.chat.id, photo)
    bot.register_next_step_handler(message, help)
    write_to_file(user_data)


@bot.message_handler(func=lambda message: True)
def aga(message):
    name = message.chat.first_name
    bot.send_message(message.chat.id, f'И тебе привет! {name}.\n')
    write_to_file(user_data)

@bot.message_handler(content_types=["sticker"])
def sticker(message):
    write_to_file(user_data)
    bot.send_message(message.chat.id, choice(phrases))



bot.polling()

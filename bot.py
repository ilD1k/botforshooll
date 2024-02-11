import telebot
from telebot.types import Message
from config import token
from jso4k import write_to_file, read_from_db
from random import choice

raspisanie = {
1: f"Расписание на завтра\n 09:00 - 09:45 Ров\n 10:00 - 10:45 История\n 11:00 - 11:45 Русский язык\n "
   f"12:00 - 12:45 География\n 13:00 - 13:45 Алгебра\n 13:55 - 14:40 Физ-ра\n 14:50 - 15:35 Информатика",

2: f"Расписание на завтра\n 08:00 - 08:45 Физика\n 09:00 - 09:45 Обществознание\n 10:00 - 10:45 Литература\n "
   f"11:00 - 11:45 Русский язык\n 12:00 - 12:45 ОБЖ\n 13:00 - 13:45 Геометрия",

3: f"Расписание на завтра\n 10:00 - 10:45 Алгебра\n 11:00 - 11:45 История\n 12:00 - 12:45 География\n 13:00 - 13:45 Геометрия\n "
   f"13:55 - 14:40 Иностранный язык",

4: f"Расписание на завтра\n 08:00 - 08:45 Иностранный язык\n 09:00 - 09:45 Русский язык\n 10:00 - 10:45 Литература\n "
   f"11:00 - 11:45 Технология\n 12:00 - 12:45 Технология\n 13:00 - 13:45 Алгебра\n 14:55 - 14:40 Физика",

5: f"Расписание на завтра\n 08:00 - 08:40 Иностранный язык\n 08:55 - 09:35 Биология\n "
   f"09:50 - 10:30 Вероятность и статистика\n 10:45 - 11:25 Русский язык\n 11:35 - 12:15 Физ-ра",

6: f"Расписание на завтра\n 08:00 - 8:40 Физ-ра\n 08:50 - 9:30 Музыка 09:40 - 10:20 Изо\n 10:30 - 11:10 Русский язык"
}



phrases = ["Уффффф чо за гипер стикер пупсик", "Эта типа малеф до травмы в 1999?", "Топ топ ножками в школу рабы системы",
           "пон", "Поньк", "мегапон", "харош", "сигма", "не будь дурак саси кулак стэтхем"]

phrasesandro = ["Приветствую! Андро", "Здаров!", "Опять сф в мид???", "Че как оно"]

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
    with open("./51144704.jpg", "rb") as gigant:
        bot.send_photo(message.chat.id, gigant)
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


@bot.message_handler(commands=["resp"], func=lambda message: message.from_user.id == 5085094693)
def day(message):
    bot.send_message(message.chat.id, "Какой день нужен?")
    bot.register_next_step_handler(message, day_of_ucheba)


def day_of_ucheba(message):
    if message.text == "Пн".lower():
        bot.send_message(message.chat.id, raspisanie[1])

    elif message.text == "Вт".lower():
        bot.send_message(message.chat.id, raspisanie[2])

    elif message.text == "Ср".lower():
        bot.send_message(message.chat.id, raspisanie[3])

    elif message.text == "Чт".lower():
        bot.send_message(message.chat.id, raspisanie[4])

    elif message.text == "Пт".lower():
        bot.send_message(message.chat.id, raspisanie[5])

    elif message.text == "Сб".lower():
        bot.send_message(message.chat.id, raspisanie[6])

    else:
        bot.register_next_step_handler(message, help)





@bot.message_handler(content_types=["text"], func=lambda message: message.from_user.id == 236725960)
def kirill(message):
    bot.send_message(message.chat.id, "Привет кирюх твое сообщение уже было отправлено Илье")
    with open("./51144704.jpg", "rb") as phata:
        bot.send_photo(message.chat.id, phata)
    bot.forward_message(5085094693, message.chat.id, message.id)
    write_to_file(user_data)

@bot.message_handler(content_types=["text"], func=lambda message: message.from_user.id == 1305549090)
def andro(message):
    bot.send_message(message.chat.id, choice(phrasesandro))
    bot.forward_message(5085094693, message.chat.id, message.id)
    with open("./pudj.png", "rb") as photo:
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

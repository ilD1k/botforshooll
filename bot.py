import telebot
from telebot.types import Message
from config import token
from jso4k import write_to_file, read_from_db

def update_user_data():
    return read_from_db()

user_data = update_user_data()

bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start(message:Message):
    bot.send_message(message.chat.id, "привет")
    bot.send_message(message.chat.id, "бот рассылает расписание уроков для 7 д класса")
    user_data[message.chat.id] = message.chat.id
    write_to_file(user_data)


@bot.message_handler(commands=["admin"], func=lambda message:message.from_user.id == 5085094693)
def admin(message):
    bot.send_message(message.chat.id, "Ку илюх"
                                      " Кидай расписание")
    bot.register_next_step_handler(message, send_raspisane)
    

def send_raspisane(message):
    user_data = update_user_data()
    for chat_id in user_data:
        bot.send_message(chat_id, message.text)

@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Все сломал или нашел не дочёты?")
    bot.send_message(message.chat.id, 'Свяжись с [создателем](https://t.me/ildics)',
                     parse_mode='Markdown', )








bot.polling()



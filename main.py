import telebot
from datetime import datetime

bot = telebot.TeleBot('5494614484:AAHiCjDUB0jkAIPZeg6Oj07Re43MJtcCf9s')
keybord1 = telebot.types.ReplyKeyboardMarkup(True)
keybord1.row('Привет','Пока', 'Дата')

def week(numb):
    if numb == 0:
        return 'Понедельник, '
    elif numb == 1:
        return 'Вторник, '
    elif numb == 2:
        return 'Среда, '
    elif numb == 3:
        return 'Четверг, '
    elif numb == 4:
        return 'Пятница, '
    elif numb == 5:
        return 'Суббота, '
    elif numb == 6:
        return 'Воскресенье, '


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'привет, давай начинать!', reply_markup=keybord1)
@bot.message_handler(content_types=['text'])


def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'И тебе привет!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'И тебе пока!')
        bot.send_message(message.chat.id, 'И тебе пока!')
    elif message.text.lower() == 'дата':
        text = f'{week(datetime.today().weekday())} {str(datetime.today())[:10]}'
        bot.send_message(message.chat.id, text)
bot.polling()


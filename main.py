from telebot import *
from datetime import datetime
from pyowm import *
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot('5494614484:AAHiCjDUB0jkAIPZeg6Oj07Re43MJtcCf9s')


language = get_default_config()
language['language'] = 'ru'
owm = OWM('98c8621246d37a8a57fdded0a17ffbd6', language)
mgr = owm.weather_manager()

def weather(city):
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    if len(weather.rain) == 0:
        rain = 0
    else:
        rain = weather.rain["1h"]
    string = f'Сейчас на улице: {weather.detailed_status}\nОблачность: {weather.clouds}%\nТекущая температура: {weather.temperature("celsius").get("temp")} градусов цельсия\nМаксимальная температура: {weather.temperature("celsius").get("temp_max")} градусов\nМинимальная температура: {weather.temperature("celsius").get("temp_min")} градусов\nСейчас ощущается: {weather.temperature("celsius").get("feels_like")} градусов\nСкорость ветра: {weather.wind().get("speed")} м/с\nЗа последний час выпало осадков: {rain} mm'
    return string

def forecast(lat,lon):
    one_call = mrg.one_call(lat=lat,lon=lon)
    text = ''
    for i in range(7):
        text += f'В этот день будет {one_call.forecast_daily[i].detailed_status}, температура воздуха дем {one_call.forecast_daily[i].temperature("celsius").get("day")} гардусов\n'
    return text


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
    keybord1 = telebot.types.ReplyKeyboardMarkup(True)
    keybord1.row('Привет!', 'Пока', 'Дата', 'Погода')
    bot.send_message(message.chat.id, 'привет, чем тебе помочь?', reply_markup=keybord1)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет!':
        bot.send_message(message.chat.id, 'И тебе привет <3')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока((')
    elif message.text.lower() == 'дата':
        text = f'{week(datetime.today().weekday())} {str(datetime.today())[:10]}'
        bot.send_message(message.chat.id, text)
    elif message.text.lower() == 'погода':
        bot.send_message(message.chat.id, 'Введите название города: ')
    elif weather(message.text).lower() is not None:
        bot.send_message(message.chat.id, weather(message.text))

@bot.message_handler(content_types=['location'])
def location(message):
    if message.location is not None:
        bot.send_message(message.chat.id, forecast(message.location.latitude, message.location.longitude))
bot.polling()


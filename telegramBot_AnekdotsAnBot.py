#TelegramBot AnekdotsAnBot

import requests
import random
import telebot
from bs4 import BeautifulSoup as b

URL = 'https://www.anekdot.ru/last/good/'               #адрес ссылки (сайт с анекдотами)
API_TOK = '5113278556:AAEVNF2nJlMdjt-pe5s7RgHP0dj-_ONrn2A'   #токен бота
def parser(url):
    r = requests.get(url)     #разрешение сервера на работу со страницей (извлечение данных из ресурса)
    s = b(r.text, 'html.parser')     #отправляем весь текст из библиотеки b в html.parser
    anekdots = s.find_all('div', class_='text')  #выкачиваем спарсерные анекдоты
    return [c.text for c in anekdots]    # возвращает вывод только текста (без тэгов)


list1 = parser(URL)                 #список анекдотов
random.shuffle(list1)               #перемешивает список (анекдоты)

bot = telebot.TeleBot(API_TOK)          #передаем классу токен

@bot.message_handler(commands=['старт']) #декаратор для запуска и обработки сообщений

def hello(message):
    bot.send_message(message.chat.id, 'Привет! Хочешь посмеяться? Быстрее вводи любую цифру в диапазоне от 1 до 9: ')
#вызываем функцию и передаем кому отправляем и отправляем сообщение для общения
@bot.message_handler(content_types=['text'])  #декоратор для получения сообщения введенного пользователем
def jokes(message): #получает сообщения от пользователя  и проверяет
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list1[0])          #первый элемент из нашего списка
        del list1[0]         #удаляем анекдот, чтобы не было повторений
    else:
        bot.send_message(message.chat.id, 'Нужно ввести любую цифру в диапазоне от 1 до 9: ')

bot.polling()          #вечный цикл с обновлением входящих сообщений от всех пользователей


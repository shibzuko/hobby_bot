# Import the necessary modules
import logging


import pytz                            # Библиотека для работы с часовым поясом
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from os import getenv                  #Позволяет получать значения переменных окружения
from dotenv import load_dotenv         #Предоставляет функцию загрузки переменных окружения из файла .env


# Импорт модулей для работы с базой данных

from sqlalchemy import create_engine                           # Импорт модулей для работы с базой данных
from sqlalchemy.ext.declarative import declarative_base        # Импорт модуля для объявления таблицы
from sqlalchemy.orm import sessionmaker                        # Импорт модуля для работы с сессиями базы данных
from datetime import datetime                                  # Импорт модуля для работы с датой и временем
from model import Users, session

#TODO: поднягивать токен надо с конфига
load_dotenv()                          #Эта функция загружает значения переменных окружения фвйла .env в текущую среду
BOT_TOKEN = getenv('TOKEN')   #Получаем значения переменной окружения с именем 'TOKEN

#Настроить ведение журнала
logging.basicConfig(level=logging.INFO)
# Create a bot instance
bot = Bot(token=BOT_TOKEN)

#Создаёт экземпляр диспетчера
dp = Dispatcher(bot)

current_time = datetime.now(pytz.timezone('Europe/Moscow'))
formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S')

message_id = None
user_id = None
is_bot = None
first_name = None
last_name = None
username = None
language_code = None
is_premium = None
text = None
date = None


# Define a message handler that echoes back messages / Определите обработчик сообщений, который повторяет сообщения
@dp.message_handler()
async def echo(message: types.Message):
    global message_id, user_id, is_bot, first_name, last_name, username, language_code, is_premium, text, date
    message_id = message.message_id
    user_id = message.chat.id
    is_bot = message.from_user.is_bot
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    username = message.chat.username
    language_code = message.from_user.language_code
    is_premium = message.from_user.is_premium
    text = message.text
    date = message.date

    exec(open('test.py').read())
    results = session.query(Users).all()
    # Вывод сообщения пользователю
    await message.answer(f'Ассаламу алейкум, {message.chat.first_name} {message.chat.last_name} '
                         f'\nСейчас: {formatted_time}\n\n\n\n{results[-1].message_id}\n\n{message.from_id}')
    session.close()


# Start the bot using the executor
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dotenv import find_dotenv, load_dotenv

from commom.bot_cmds_list import private
from handlers.admin_private import admin_router
from handlers.user_group import user_group_router
from handlers.user_private import user_private_router

'''                 Основной файл запуска настроек и конфигураций'''

load_dotenv(find_dotenv()) # Загрузить переменную окружения

ALLOWED_UPDATES = ['message', 'edited_message'] # Допускаемык апдейты

bot = Bot(token=os.getenv('TOKEN', default=DefaultBotProperties(parse_mode=ParseMode.HTML))) # Передать токен указать парс мод ред текста
bot.my_admins_list = []

dp = Dispatcher()

dp.include_router(user_private_router) # Подключаем роутер юзер приват
dp.include_router(user_group_router)# подключаем юзер груп роутер
dp.include_router(admin_router) # подключаем юзер груп админ


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats()) # Удалить кнопку меню
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats()) # Установить кнопку меню с командами
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES) # Запускает бота в работу станет ждать апдейты асинхронно

asyncio.run(main()) # Запускает функцию асинхронно
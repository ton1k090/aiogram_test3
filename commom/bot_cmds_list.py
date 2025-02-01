from aiogram.types import BotCommand

'''Создать список кнопок меню меню и добавить в bot.set_my_commands'''

private = [
    BotCommand(command='menu', description='Посмотреть меню'),
    BotCommand(command='about', description='О нас'),
    BotCommand(command='payment', description='Варианты оплаты'),
    BotCommand(command='shipping', description='Варианты доставки'),
]
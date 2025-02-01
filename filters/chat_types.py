'''Фильтровать события в зависимости в каком чате оно написано'''

from aiogram.filters import Filter
from aiogram import types, Bot

'''Файл для выбора фильтра к боту или чату'''


class ChatTypeFilter(Filter):
    def __init__(self, chat_types: list[str]) -> None:
        self.chat_types = chat_types

    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in self.chat_types


class IsAdmin(Filter):
    '''Проверка на админа'''
    def __init__(self) -> None:
        pass

    async def __call__(self, message: types.Message, bot: Bot) -> bool: # принимаем мессадж и прокидываем бота
        return message.from_user.id in bot.my_admins_list # получаем юзер ай-ди и есть ли он в админах
'''Здесь будем хранить хендлеры для работы бота в группах'''
from string import punctuation # строка со всеми знаками пунктуации
from aiogram import F, types, Router, Bot
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter


'''                  Файл хендлеров относящийся к общению с группой'''

user_group_router = Router() # создаем роутер
user_group_router.message.filter(ChatTypeFilter(['group', 'supergroup'])) # Навесить фильтры на роуты и выбрать группы
user_group_router.edited_message.filter(ChatTypeFilter(["group", "supergroup"]))

restricted_words = {'кабан', 'хомяк', 'выхухоль'} # слова исключения


@user_group_router.message(Command("admin")) # реагируем на команду админ
async def get_admins(message: types.Message, bot: Bot):
    chat_id = message.chat.id # вытаскиваем из месседж чат айди
    admins_list = await bot.get_chat_administrators(chat_id)
    #просмотреть все данные и свойства полученных объектов
    #print(admins_list)
    # Код ниже это генератор списка, как и этот x = [i for i in range(10)]
    admins_list = [
        member.user.id
        for member in admins_list
        if member.status == "creator" or member.status == "administrator"
    ]
    bot.my_admins_list = admins_list # навешиваем новый список
    if message.from_user.id in admins_list:
        await message.delete() # если пользователь админ команду просто удалим
    #print(admins_list)


def clean_text(text: str):
    return text.translate(str.maketrans('', '', punctuation)) # убирает все знаки пунктуации


@user_group_router.edited_message
@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(clean_text(message.text.lower()).split()): # если слово есть в сообщении
        await message.answer(f'{message.from_user.first_name}, предупреждение') # отправляет нарушевшему юзеру
        await message.delete() # удалить слово




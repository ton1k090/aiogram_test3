import emoji
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command, or_f
from aiogram import types, Router, F
from filters.chat_types import ChatTypeFilter
from kbds import reply
from aiogram.utils.formatting import as_list, as_marked_section, Bold # для форматирования текста

'''                 Файл хендлеров относящийся к общению с ботом'''

user_private_router = Router() # Создаем роутер вместо диспетчера
user_private_router.message.filter(ChatTypeFilter(['private'])) # Навесить фильтры на роуты и выбрать группы


@user_private_router.message(CommandStart()) # реагировать на команду старт  (должна быть первой )
async def start_cmd(message: types.Message):
    await message.answer('Привет я виртуальный помощник', reply_markup=reply.get_keyboard( # новый вид меню
        'Меню',
        'О нас',
        'Варианты оплаты',
        'Варианты доставки',
        placeholder='Что интересует',
        sizes=(2, 2)
    ),
                         )
    # await message.answer('Привет я виртуальный помощник',
    #                      reply_markup=reply.start_kb2.as_markup(
    #                          resize_keyboard=True
    #                      )) # Клавиатура со способом 2


@user_private_router.message(or_f(Command('menu'), (F.text.lower == 'меню'))) # реагировать определенную команду - menu,  or_f - или
async def menu_cmd(message: types.Message):
    # await bot.send_message(message.from_user.id, 'answer') # Подобие реализации ответа в сухом виде
    await message.answer('Вот меню:', reply_markup=reply.del_kbd) # Вернуть этот текст и удалить клаву
    # await message.reply(message.text) # Ответить с упоминанием автора


@user_private_router.message(F.text.lower() == 'о нас') # реагировать определенную команду о нас
@user_private_router.message(Command('about')) # реагировать определенную команду - about
async def about_cmd(message: types.Message):
    await message.answer('О нас:') # Вернуть этот текст


@user_private_router.message(F.text.lower() == 'варианты оплаты') # реагировать определенную команду варианты оплаты
@user_private_router.message(Command('payment')) # реагировать определенную команду - payment
async def payment_cmd(message: types.Message):
    '''Сформирует промаркерованый список'''
    text = as_marked_section( # оберните элементы с промаркерованным списком
        Bold('Варианты оплаты'),
        'Картой в боте',
        'При получении карта/кэщ',
        'В заведении',
        marker= '✅' # маркер

    )
    await message.answer(text.as_html()) # Вернуть этот текст указать вид парса


@user_private_router.message((F.text.lower().contains('доставк')) | (F.text.lower() == 'варианты доставки')) # реагировать определенную команду доставки
@user_private_router.message(Command('shipping')) # реагировать определенную команду - shipping
async def shipping_cmd(message: types.Message):
    text = as_list(as_marked_section(  # оберните элементы с промаркерованным списком
        Bold('Варианты доставки'), # Как можно
        'Курьер',
        'Самовывоз',
        'На месте',
        marker='✅'  # маркер
    ),
    as_marked_section(
        Bold('Нельзя'), # Как нельзя
        'Почта',
        'Голуби',
        marker='⛔️'
    ),
    sep='\n--------------\n' # Разделитель между можно и нельзя
    )
    await message.answer(text.as_html()) # Вернуть этот текст отформатировав парс модом


@user_private_router.message(F.contact) # для отлова контакта
async def get_contact(message: types.Message):
    await message.answer(f'номер получен')
    await message.answer(str(message.contact)) # вернуть контакт


@user_private_router.message(F.location) # для отлова местоположения
async def get_contact(message: types.Message):
    await message.answer(f'локация получена')
    await message.answer(str(message.location)) # вернуть местоположение

'''                    Закоментированый старый код'''

# @user_private_router.message() # реагировать на любой текст
# async def echo(message: types.Message):
#     # await bot.send_message(message.from_user.id, 'answer') # Подобие реализации ответа в сухом виде
#     await message.answer(message.text) # Вернуть тот же текст
#     # await message.reply(message.text) # Ответить с упоминанием автора

# @user_private_router.message(F.text.lower() == 'варианты доставки') # реагировать определенную команду
# async def shipping_cmd(message: types.Message):
#     await message.answer('Это магический фильтр') # Вернуть этот текст


# @user_private_router.message(F.text.lower().contains() == 'варианты доставки') # реагировать определенную команду
# async def shipping_cmd(message: types.Message):
#     await message.answer('Это магический фильтр 2') # Вернуть этот текст



# @user_private_router.message((F.text.lower().contains() == 'доставк') | (F.text.lower() == 'варианты доставки')) # реагировать определенную команду через запятую = и
# async def shipping_cmd(message: types.Message):
#     await message.answer('Это магический фильтр') # Вернуть этот текст
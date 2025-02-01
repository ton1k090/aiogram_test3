'''Reply клавиатура'''
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder

''' 1 способ ReplyKeyboardMarkup: Массив из массивов кнопок один список - одна строка кнопок'''
# start_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='Меню'),
#             KeyboardButton(text='О нас'),
#
#         ],
#         [
#             KeyboardButton(text='Варианты доставки'),
#             KeyboardButton(text='Варианты оплаты'),
#         ]
#     ],
#     resize_keyboard=True,
#     input_field_placeholder='main menu'
# )
#
# del_kbd = ReplyKeyboardRemove()
#
#
# '''способ 2 ReplyKeyboardBuilder:'''
#
# start_kb2 = ReplyKeyboardBuilder()
# start_kb2.add(
#     KeyboardButton(text='Меню'),
#             KeyboardButton(text='О магазине'),
#             KeyboardButton(text='Варианты доставки'),
#             KeyboardButton(text='Варианты оплаты'),
# )
# start_kb2.adjust(2, 2).as_markup() # По 2 кнопки в ряду
#
#
# '''Способ расширения клавиатуры'''
# start_kb3 = ReplyKeyboardBuilder()
# start_kb3.attach(start_kb2) # Добавить старую клавиатуру в новую для расширения
# start_kb3.row(KeyboardButton(text='Оставить отзыв'),)
# start_kb3.adjust(2, 2)
#
# '''Еще одна клавиатура'''
#
# test_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='Создать опрос', request_poll=KeyboardButtonPollType()) # Сделать опрос
#         ],
#         [
#             KeyboardButton(text='Отправить номер:', request_contact=True), # Запросить контакт
#             KeyboardButton(text='Отправить локацию', request_location=True) # Запросить локацию
#         ]
#     ],
#     resize_keyboard=True
# )

'''           Основной способ работать с клавиатурами'''


def get_keyboard(
        *btns: str, # Передаем кнопки из клавиатуры
        placeholder: str = None, # Передаем плейсхолдер из списка
        request_contact: int = None, # Передается индекс кнопки
        request_location: int = None, # Передается индекс кнопки
        sizes: tuple[int] = (2,),
):
    ''''Функция будет генерировать любые кнопки вызывая их в хендлере'''
    '''
    Parameters request_contact and request_location must be as indexes of btns args for buttons you need.
    Example:
    get_keyboard(
            "Меню",
            "О магазине",
            "Варианты оплаты",
            "Варианты доставки",
            "Отправить номер телефона"
            placeholder="Что вас интересует?",
            request_contact=4,
            sizes=(2, 2, 1)
        )
    '''
    keyboard = ReplyKeyboardBuilder() # Формируется клавиатура

    for index, text in enumerate(btns, start=0):

        if request_contact and request_contact == index:
            keyboard.add(KeyboardButton(text=text, request_contact=True))

        elif request_location and request_location == index:
            keyboard.add(KeyboardButton(text=text, request_location=True))
        else:

            keyboard.add(KeyboardButton(text=text))

    return keyboard.adjust(*sizes).as_markup(
        resize_keyboard=True, input_field_placeholder=placeholder)
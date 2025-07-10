from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

ik = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Ввести дату', callback_data = 'write data')],
    [InlineKeyboardButton(text='Завершить работу', callback_data = 'finish work')]])


# kb = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='Испытать меня')],
#     [KeyboardButton(text='Завершить работу')]
# ], resize_keyboard=True, input_field_placeholder = 'Выберите вариант...')

ik2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='На старт', callback_data = 'start work')]])


kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Испытать меня', callback_data = 'try me')],
    [InlineKeyboardButton(text='Завершить работу', callback_data = 'finish work')]])
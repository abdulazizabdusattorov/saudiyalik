from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menuStart = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Qabullar'),
            KeyboardButton(text='Ma`lumotlar' ),
        ],
        [
            KeyboardButton(text='A`loqa'),
            KeyboardButton(text='Yordam'),
        ],
    ],
    resize_keyboard=True
)
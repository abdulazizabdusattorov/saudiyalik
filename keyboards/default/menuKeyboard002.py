from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Ma`lumotlar"'),
            KeyboardButton(text='Imtiyozlar'),
        ],
        [
            KeyboardButton(text='Ummul Quro'),
            KeyboardButton(text='Xolid'),
        ],
        [
            KeyboardButton(text='Malik Abdulaziz'),
            KeyboardButton(text='Imom Muhammad Bin Saud'),
        ],
[
            KeyboardButton(text='Boshiga'),
        ],

    ],
    resize_keyboard=True
)
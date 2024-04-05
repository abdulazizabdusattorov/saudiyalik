from aiogram.types import ReplyKeyboardMarkup,KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text='Amira Nura'),
            KeyboardButton(text='Madina islom universiteti'),
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
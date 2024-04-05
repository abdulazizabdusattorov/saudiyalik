from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menuPython = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="00 KIRISH"),
            KeyboardButton(text="01 KERAKLIK DASTURLAR"),
            KeyboardButton(text="02 HELLO WORLD"),
        ],
        [
            KeyboardButton(text="Ortga"),
            KeyboardButton(text="Boshiga"),
        ],
    ],
    resize_keyboard=True
)
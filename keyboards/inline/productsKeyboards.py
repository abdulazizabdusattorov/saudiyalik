from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup

#1-usul

categoryMenu001 = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ma`lumotlar",callback_data="Ma`lumot olish"),
            InlineKeyboardButton(text="Imtiyozlar", callback_data="Imtiyozni bilish"),
        ],
        [
            InlineKeyboardButton(text="Keraklik hujjatlar", callback_data='Keraklik hujjatlar haqida'),
            InlineKeyboardButton(text="Qabul shartlari", callback_data='Qabul shartlari haqida'),
        ],
[
            InlineKeyboardButton(text="A`loqa", url='https://mohirdev.uz'),
        ],
        [
            InlineKeyboardButton(text="Qidirish", switch_inline_query_current_chat=""),
        ],
        [
            InlineKeyboardButton(text="Ulashish", switch_inline_query="Zo`r bot ekan kirib start tugmasini bosing!"),
        ],
    ])
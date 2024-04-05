from aiogram.dispatcher.filters import Command,Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default.menuKeyboard import menu
from keyboards.default.pythonKeyboard import menuPython
from keyboards.default.start import menuStart
from keyboards.inline.productsKeyboards import categoryMenu001

from loader import dp

@dp.message_handler(Text("Qabullar"))
async def show_menu(message: Message):
    await message.answer("Universitetlarni tanlang!", reply_markup=menu)


@dp.message_handler(Text("Boshiga"))
async def show_menu(message: Message):
    await message.answer("Asosiy bo`limga qaytdingiz!", reply_markup=menuStart)


@dp.message_handler(Text("Ma`lumotlar"))
async def show_menu(message: Message):
    await message.answer("Arab davlatlari Unıversıtetları va akademiyalariga oʻqiş hujjatlarını toşırıb beramız. Öqış haqida eng sara maʼlumot bızda.\n \n"
                         "A`loqa uchun: @King_salman_talabasi", reply_markup=menuStart)

@dp.message_handler(Text("A`loqa"))
async def show_menu(message: Message):
    await message.answer("A`loqa uchun: @King_salman_talabasi", reply_markup=menuStart)

@dp.message_handler(Text("Yordam"))
async def show_menu(message: Message):
    await message.answer("Quyidagi menulardan birini tanlang!👇", reply_markup=menuStart)


@dp.message_handler(Text("Amira Nura"))
async def show_menu(message: Message):
    await message.answer(f"<b>Amira Nura haqida ma`lumotlar</b> \n"
                         "AMIRA-NURA QIZLAR UNIVERSITETNING YO'NALISHLARI \n \n \n"
                         "🤎SHARIAT FAKULTETI \n"
                         "[Barcha shari'y yo'nalishlarni o'z ichiga oladi]"
                         "🤎MUHANDISLIK FAKULTETI\n"
                         "🤎Elektron aloqa\n"
                         "🤎Sanoat muhandisligi\n\n\n"
                         "🤎FAN FAKULTETI \n"
                         "🤎Biologiya\n"
                         "🤎Kimyo\n"
                         "🤎Fizika\n"
                         "🤎Matematika\n\n\n"
                         "", reply_markup=menu)
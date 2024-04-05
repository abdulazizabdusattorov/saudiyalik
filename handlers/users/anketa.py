from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.personalData import PersonalData

@dp.message_handler(Command('anketa'))

async def enter_test(message: types.Message):
    await message.answer("To`liq ismingizni kiriting!")
    await PersonalData.fullName.set()

@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message: types.Message, state:FSMContext):
    fullname = message.text
    await state.update_data(name=fullname)

    await state.update_data(
        {"name":fullname}
    )

    await message.answer("Email manzil kiriting!")
    await PersonalData.next()
    #await PersonalData.email.set()

@dp.message_handler(state=PersonalData.email)
async def answer_email(message: types.Message, state:FSMContext):
    email = message.text

    await state.update_data(
        {"email": email}
    )

    await message.answer("Telefon raqam kiriting!")

    await PersonalData.next()

@dp.message_handler(state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {'phone': phone}
    )

    #Ma`lumotlarni qayta o`qish

    data = await state.get_data()
    name = data.get("name")
    email = data.get('email')
    phone = data.get('phone')

    msg = "Quyidagi ma`lumotlar qabul qilindi!\n \n"
    msg += f"Ismingiz: {name}\n \n"
    msg += f"Emailingiz: {email}\n \n"
    msg += f"Tel raqamingiz: {phone}\n \n"
    await message.answer(msg)

    await state.finish()



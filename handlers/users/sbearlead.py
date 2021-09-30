import  logging

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from keyboards.inline.choice_btn import choice
from loader import dp


@dp.message_handler(Command("inline_buttons_1"))
async def show_items(message: Message):
    await message.answer(text="Edit @Sberleadbot info\n\n"
                              "Name: Бот для заданий на курсе Udemy\n"
                              "Description: ?\n"
                              "About: ?\n"
                              "Botpic: ? no botpic\n"
                              "Commands: no commands yet",
                         reply_markup=choice)



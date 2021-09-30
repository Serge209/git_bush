import logging


from aiogram.dispatcher.filters import Command
from aiogram.types import Message,CallbackQuery

from keyboards.inline.fruits import fruit_callback

from keyboards.inline.fruits import fruit




from loader import dp



@dp.message_handler(Command("item"))
async def show_item(message:Message):
    await message.answer(text="Мандарин",
                         reply_markup=fruit)

@dp.callback_query_handler(text_contains="orange")
async def buying_orange(call:CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logging.info(f"{callback_data=}")

    await call.message.answer("Покупай товар номер 1!")

@dp.callback_query_handler(text_contains="like")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logging.info(f"f{callback_data=}")
    await call.message.answer("Вам понравился этот товар!")

@dp.callback_query_handler(text_contains="dislike")
async def buying_apples(call: CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    logging.info(f"f{callback_data=}")
    await call.message.answer("Вам не понравился этот товар!")


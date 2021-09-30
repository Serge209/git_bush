from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback

choice = InlineKeyboardMarkup(inline_keyboard=[
 [
     InlineKeyboardButton(text="Edit Name", callback_data="edit:name"),
     InlineKeyboardButton(text="Edit Description", callback_data="edit:descr")

 ],
 [
     InlineKeyboardButton(text="Edit About", callback_data="edit:about"),
     InlineKeyboardButton(text="Edit Botpic", callback_data="edit:botpic")
 ],
 [
     InlineKeyboardButton(text="Edit Commands", callback_data="edit:commands"),
     InlineKeyboardButton(text="<<Back to Bot", callback_data="edit:back")
 ]
])
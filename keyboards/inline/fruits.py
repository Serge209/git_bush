from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import fruit_callback

fruit = InlineKeyboardMarkup(inline_keyboard=[
 [
     InlineKeyboardButton(text="Купить товар", callback_data="item_name:orange")
 ],
 [
     InlineKeyboardButton(text="like 🦦", callback_data="item_name:like"),
     InlineKeyboardButton(text="dislike", callback_data="item_name:dislike")
 ],
 [
     InlineKeyboardButton(text="Поделиться с другом", url="https://rozetka.com.ua/champion_a00225/p27223057")
 ]
])


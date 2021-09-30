from aiogram.utils.callback_data import CallbackData

buy_callback = CallbackData("buy", "item_name", "quantity")

edit_callback = CallbackData("name", "about", "commands", "descr", "botpic", "back")

fruit_callback = CallbackData("buy", "item_name", "like", "dislike", "share")
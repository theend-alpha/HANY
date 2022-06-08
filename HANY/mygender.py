from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery, Message
from Alone import AlphaIsAlone

@Client.on_message(filters.command(["mygender", "mygender@nothehe_bot"]) & ~filters.via_bot & ~filters.forwarded & ~filters.edited)
async def mygender(_, message: Message):
    global i_id
    i_id = message.from_user.id
    i_m = (await _.get_users(i_id)).mention
    c_id = message.chat.id
    await _.send_message(c_id, f"{i_m}, Set your gender !", reply_markup=InlineKeyboardMarkup(AlphaIsAlone.gender_markup))

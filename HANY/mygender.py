from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery, Message
from Alone import AlphaIsAlone
from HANY.AlphaDB.genders_adb import id_is_male, id_is_female, flee

@Client.on_message(filters.command(["mygender", "mygender@nothehe_bot"]) & filters.private & ~filters.edited &filters.incoming)
async def mygender(_, message: Message):
    global i_id
    i_id = message.from_user.id
    i_m = (await _.get_users(i_id)).mention
    c_id = message.chat.id
    await _.send_message(c_id, f"{i_m}, Set your gender !", reply_markup=InlineKeyboardMarkup(AlphaIsAlone.gender_markup))

@Client.on_message(filters.command(["flee", "flee@nothehe_bot"]) & filters.private & ~filters.edited & filters.incoming)
async def flew(_, message: Message):
    i_id = message.from_user.id
    i_fn = message.from_user.first_name
    c_id = message.chat.id
    if id_is_male(i_id):
        flee(i_id)
        await _.send_message(c_id, f"gender status for {i_fn} is updated to None")
    elif id_is_female(i_id):
        flee(i_id)
        await _.send_message(c_id, f"gender status for {i_fn} is updated to None")

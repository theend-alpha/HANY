from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery, Message
from Alone import AlphaIsAlone
from HANY.AlphaDB.genders_adb import id_is_male, id_is_female, flee, get_males, get_females

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
    else:
        await _.send_message(c_id, f"{message.from_user.mention}, your gender is alread None\n\n Try: /mygender to set !")

@Client.on_message(filters.command(["users", "users@nothehe_bot"]) & ~filters.edited)
async def _users(_, message: Message)
    m_c = await get_males()
    f_c = await get_females()
    await message.reply(f""" Bot Users \n\n No of males = {m_c} \n No of females = {f_c} """)

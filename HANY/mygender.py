from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery, Message
from Alone import AlphaIsAlone
from HANY.AlphaDB.genders_adb import MALES, FEMALES, rmv_male, rmv_female, get_males, get_females

B_U = """ Bot Users \n\n No of males = {} \n No of females = {} """

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
    if i_id in MALES:
        rmv_male(i_id)
        await _.send_message(c_id, f"gender status for {i_fn} is updated from male to None")
    elif i_id in FEMALES:
        rmv_female(i_id)
        await _.send_message(c_id, f"gender status for {i_fn} is updated from female to None")
    else:
        await _.send_message(c_id, f"{message.from_user.mention}, your gender is alread None\n\n Try: /mygender to set !")

@Client.on_message(filters.command(["users", "users@nothehe_bot"]) & ~filters.edited)
async def _users(_, message: Message):
    m_c = get_males()
    f_c = get_females()
    await message.reply(B_U.format(m_c, f_c))

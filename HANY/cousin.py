from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup
from HANY.AlphaDB.cousins_adb import add_cousin, rmv_cousin, are_cousins, cousins_list_for, add_to_waiting, rmv_from_waiting, id_is_waiting, WAITING_LIST
from HANY.AlphaDB.genders_adb import MALES, FEMALES, id_is_male, id_is_female
from Alone import AlphaIsAlone

ACCEPT_TEXT = "{} {} added back {} {} as their cousin !"

@Client.on_message(filters.command(["cousin", "cousin@nothehe_bot"]) & filters.group & ~filters.edited & ~filters.forwarded & ~filters.via_bot)
async def csn(_, message: Message):
    i_id = message.from_user.id
    c_id = message.chat.id
    i_m = message.from_user.mention
    if message.reply_to_message.from_user.is_bot:
        return
    f_id = message.reply_to_message.from_user.id
    if f_id == i_id:
        await message.reply("You can't add yourself as your cousin 🥱 ")
    f_m = (await _.get_users(f_id)).mention
    id_is_waiting(f_id)
    id_is_male(i_id)
    id_is_male(f_id)
    id_is_female(i_id)
    id_is_female(f_id)
    if f_id in WAITING_LIST:
        await _.send_message(c_id, ACCEPT_TEXT.format(" 👦 " if i_id in MALES else " 👧 ", i_m, " 👦 " if f_id in MALES else " 👧 ", f_m))

    

from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup
from HANY.AlphaDB.cousins_adb import add_cousin, rmv_cousin, are_cousins, cousins_list_for
from HANY.AlphaDB.genders_adb import MALES, FEMALES, id_is_male, id_is_female
from Alone import AlphaIsAlone


@Client.on_message(filters.command(["cousin", "cousin@nothehe_bot"]) & filters.group & ~filters.edited & ~filters.forwarded & ~filters.via_bot)
async def csn(_, message: Message):
    global i_id
    global f_id
    global f_m
    global i_m
    i_id = message.from_user.id
    c_id = message.chat.id
    i_m = message.from_user.mention
    if message.reply_to_message.from_user.is_bot:
        return
    f_id = message.reply_to_message.from_user.id
    if f_id == i_id:
        await message.reply("You can't add yourself as your cousin 🥱 ")
    f_m = (await _.get_users(f_id)).mention
    is_id_male(i_id)
    is_id_female(i_id)
    if i_id in MALES:
        await _.send_message(c_id, f"{i_m} wants {f_m} as his cousin. \n\nTry: Reply < /cousin > to add back !")

    

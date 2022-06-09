from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery
from HANY.AlphaDB.cousins_adb import add_cousin, rmv_cousin, are_cousins, cousins_list_for
from HANY.AlphaDB.genders_adb import MALES, FEMALES, id_is_male, id_is_female

@Client.on_message(filters.command(["cousin", "cousin@nothehe_bot"]) & filters.group & ~filters.edited & ~filters.forwarded & ~filters.via_bot)
async def csn(_, message: Message):
    global i_id
    global f_id
    i_id = message.from_user.id
    c_id = message.chat.id
    i_m = message.from_user.mention
    if message.reply_to_message:
        f_id = message.reply_to_message.from_user.id
    else:
        try:
            f_id = int(message.text)
        except:
            message.reply("Omfoo Try: /cousin < user_id > ")
    f_m = (await _.get_users(f_id)).mention
    id_is_male(i_id)
    id_is_female(i_id)
    if i_id in MALES:
        await _.send_message(c_id, f"{i_m} wants {f_m} as his cousin...", reply_markup=InlineKeyboardMarkup(AlphaIsAlone.cousin_markup))
        MALES.remove(i_id)
    elif i_id in FEMALES:
        await _.send_message(c_id, f"{i_m} wants {f_m} as her cousin...", reply_markup=InlineKeyboardMarkup(AlphaIsAlone.cousin_markup))
        FEMALES.remove(i_id)
    else:
        await _.send_message(c_id, f"{i_m}, your gender is unspecified, please set it first !", reply_markup=InlineKeyboardMarkup(AlphaIsAlone.set_gender_markup))

@Client.on_callback_query()
async def csnback(_: Client, query: CallbackQuery):
    q_id = query.from_user.id
    if f_id == q_id:
        if query.data == "addc":
            add_cousin(q_id, i_id)
            add_cousin(i_id, q_id)
            await query.edit 

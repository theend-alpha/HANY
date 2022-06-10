from pyrogram import Client, filters
from pyrogram.types import Message, CallbackQuery, InlineKeyboardMarkup
from HANY.AlphaDB.cousins_adb import add_cousin, rmv_cousin, are_cousins, cousins_list_for, add_to_waiting, rmv_from_waiting, id_in_waiting, WAITING_LIST
from HANY.AlphaDB.genders_adb import MALES, FEMALES, id_is_male, id_is_female
from Alone import AlphaIsAlone

ACCEPT_TEXT = "✨ {}{} 💫 added back ✨ {}{} 💫 as their cousin !"

INIT_TEXT = """✨ {}{} 💫 wants ✨ {}{} 💫 as {} cousin.. \n\n Try: reply < /cousin > to add back !""" 

ABANDON_TEXT = "{}{} abandoned {}{} as their cousin.."

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
    id_in_waiting(f_id, i_id)
    id_is_male(i_id)
    id_is_male(f_id)
    id_is_female(i_id)
    id_is_female(f_id)
    if f_id in WAITING_LIST:
        add_cousin(i_id, f_id)
        add_cousin(f_id, i_id)
        rmv_from_waiting(f_id, i_id)
        await _.send_message(c_id, ACCEPT_TEXT.format(" 👦 " if i_id in MALES else " 👧 ", i_m, " 👦 " if f_id in MALES else " 👧 ", f_m))
        WAITING_LIST.remove(f_id)
    elif i_id in MALES and f_id not in WAITING_LIST:
        add_to_waiting(i_id, f_id)
        await _.send_message(c_id, INIT_TEXT.format(" 👦 ", i_m, " 👧 " if f_id in FEMALES else " 👦 ", f_m, "his"))
    elif i_id in FEMALES and f_id not in WAITING_LIST:
        add_to_waiting(i_id, f_id)
        await _.send_message(c_id, INIT_TEXT.format(" 👧 ", i_m, " 👧 " if f_id in FEMALES else " 👦 ", f_m, "her"))
    else:
        await message.reply(" Your gender is unspecified, Try: /mygender 👇 ", reply_markup=InlineKeyboardMarkup(AlphaIsAlone.set_gender_markup))
    MALES.clear()
    FEMALES.clear()

@Client.on_message(filters.command(["leavecousin", "leavecousin@nothehe_bot"]) & filters.group & ~filters.edited & ~filters.forwarded & ~filters.via_bot)
async def eww(_, message: Message):
    i_id = message.from_user.id
    f_id = message.reply_to_message.from_user.id
    i_m = message.from_user.mention
    f_m = message.reply_to_message.from_user.mention
    id_is_male(i_id)
    id_is_male(f_id)
    rmv_cousin(i_id, f_id)
    rmv_cousin(f_id, i_id)
    await _.send_message(message.chat.id, ABANDON_TEXT.format(" 👦 " if i_id in MALES else " 👧 ", i_m, " 👦 " if f_id in MALES else " 👧 ", f_m))
    MALES.clear()

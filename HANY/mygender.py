from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery, Message
from Alone import AlphaIsAlone

MALES = []

FEMALES = []

OMFOO = []

@Client.on_message(filters.command(["mygender", "mygender@nothehe_bot"]) & ~filters.via_bot & ~filters.forwarded & ~filters.edited)
async def mygender(_, message: Message):
    global i_id
    i_id = message.from_user.id
    i_m = (await _.get_users(i_id)).mention
    c_id = message.chat.id
    appended = OMFOO.append(i_id)
    if appended:
        await _.send_message(-1001732078344, f"{i_id} appended to list")
    else:
        await _.send_mesaage(-1001732078344, "append failed")
    await _.send_message(c_id, f"{i_m}, choose your gender", reply_markup=InlineKeyboardMarkup(AlphaIsAlone.gender_markup))

@Client.on_callback_query(filters.regex("male"))
async def Male(_: Client, query: CallbackQuery):
    if query.from_user.id == i_id:
        if i_id in FEMALES:
            FEMALES.remove(i_id)
        if i_id in MALES:
            return
        MALES.append(i_id)
        await query.message.edit("your gender is updated to male 👦 ")

@Client.on_callback_query(filters.regex("female"))
async def Female(_: Client, query: CallbackQuery):
    if query.from_user.id == i_id:
        if i_id in MALES:
            MALES.remove(i_id)
        if i_id in FEMALES:
            return
        FEMALES.append(i_id)
        await query.message.edit("your gender is updated to female 👧 ")

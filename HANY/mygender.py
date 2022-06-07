from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery, Message
from Alone import AlphaIsAlone

MALES = []

FEMALES = []

@Client.on_message(filters.command(["mygender", "mygender@nothehe_bot"]) & ~filters.via_bot & ~filters.forwarded & ~filters.edited)
async def mygender(_, message: Message):
    global i_id
    global c_id
    i_id = message.from_user.id
    i_m = (await _.get_users(i_id)).mention
    c_id = message.chat.id
    await _.send_message(c_id, f"{i_m}, choose your gender", reply_markup=InlineKeyboardMarkup(AlphaIsAlone.gender_markup))

@Client.on_callback_query()
async def genderback(_: Client, query: CallbackQuery):
    q_id = query.from_user.id
    if i_id == q_id:
        if query.data == "male":
            if i_id in FEMALES:
                FEMALES.remove(i_id)
            if i_id in MALES:
                return
            MALES.append(i_id)
            await query.message.edit_text("your gender is updated to male 👦 ")
        elif query.data == "female":
            if i_id in MALES:
                MALES.remove(i_id)
            if i_id in FEMALES:
                return
            FEMALES.append(i_id)
            await query.message.edit_text("your gender is updated to female 👧 ")

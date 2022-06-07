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
    msg_id = query.message.message_id
    if query.data == "male":
        if q_id == i_id:
            if q_id in FEMALES:
                FEMALES.remove(q_id)
            if q_id in MALES:
                return
            MALES.append(q_id)
            await _.edit_message_text(chat_id=c_id, message_id=msg_id, text="your gender is updated to male 👦 ")
    elif query.data == "female":
        if q_id == i_id:
            if q_id in MALES:
                MALES.remove(q_id)
            if q_id in FEMALES:
                return
            FEMALES.append(q_id)
            await _.edit_message_text(chat_id=c_id, message_id=msg_id, text="your gender is updated to female 👧 ")

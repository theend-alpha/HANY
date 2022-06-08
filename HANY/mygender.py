from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery, Message
from Alone import AlphaIsAlone
from HANY.AlphaDB.genders_adb import add_male, add_female

@Client.on_message(filters.command(["mygender", "mygender@nothehe_bot"]) & ~filters.via_bot & ~filters.forwarded & ~filters.edited)
async def mygender(_, message: Message):
    global i_id
    i_id = message.from_user.id
    i_m = (await _.get_users(i_id)).mention
    c_id = message.chat.id
    await _.send_message(c_id, f"{i_m}, Set your gender !", reply_markup=InlineKeyboardMarkup(AlphaIsAlone.gender_markup))

@Client_on_callback_query()
async def genderback(_: Client, query: CallbackQuery):
    if i_id == query.from_user.id:
        if query.data.startswith("male"):
            if query.data == "male":
                add_male(query.from_user.id)
                await _.edit_message_text(query.message.chat.id, query.message.message_id, "your gender is updated to male 👦 ")

        elif query.data == "female":
            add_female(query.from_user.id)
            await _.edit_message_text(query.message.chat.id, query.message.message_id, "your gender is updated to female 👧 ")

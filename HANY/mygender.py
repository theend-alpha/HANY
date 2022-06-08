from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, CallbackQuery, Message
from Alone import AlphaIsAlone

@Client.on_message(filters.command(["mygender", "mygender@nothehe_bot"]) & ~filters.via_bot & ~filters.forwarded & ~filters.edited)
async def mygender(_, message: Message):
    global i_id
    i_id = message.from_user.id
    i_m = (await _.get_users(i_id)).mention
    c_id = message.chat.id
    await _.send_message(c_id, f"{i_m}, Set your gender !", reply_markup=InlineKeyboardMarkup(AlphaIsAlone.gender_markup))

@Client.on_callback_query()
async def genderback(_: Client, query: CallbackQuery):
    if i_id == query.from_user.id:
        if query.data == "male"
            male_added = add_male(i_id)
            if male_added:
                await query.message.edit_text("your gender is updated to male 👦 ")
            else:
                await query.message.edit_text("Error occurred, Try: complain to alpha")
        elif query.data == "female"
            female_added = add_female(i_id)
            if female_added:
                await query.message.edit_text("your gender is updated to female 👧 ")
            else:
                await query.message.edit_text("Error occurred, Try: complain to alpha")


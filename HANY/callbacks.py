from Data import Data
from Yashvi import Keshav
from pyrogram import Client
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from HANY.AlphaDB.genders_adb import add_male, add_female, rmv_female, rmv_male

@Client.on_callback_query()
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    user = await bot.get_me()
    # user_id = callback_query.from_user.id
    mention = user["mention"]
    query = callback_query.data.lower()
    if query.startswith("home"):
        if query == 'home':
            chat_id = callback_query.from_user.id
            message_id = callback_query.message.message_id
            await bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text=Data.START.format(callback_query.from_user.mention, mention),
                disable_web_page_preview=True,
                reply_markup=InlineKeyboardMarkup(Keshav.alpha_buttons),
            )
    elif query == "credits":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Keshav.CREDITS,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Keshav.home_button),
        )
    elif query == "cmda":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text=Keshav.CMDA,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Keshav.home_button),
        )
    elif query == "male":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        rmv_male(chat_id)
        rmv_female(chat_id)
        add_male(chat_id)
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Your gender is updated to male ???? ",
        )
    elif query == "female":
        chat_id = callback_query.from_user.id
        message_id = callback_query.message.message_id
        rmv_female(chat_id)
        rmv_male(chat_id)
        add_female(chat_id)
        await bot.edit_message_text(
            chat_id=chat_id,
            message_id=message_id,
            text="Your gender is updated to female ????  ",
        )

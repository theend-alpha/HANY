from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message
from Yashvi import Keshav

photo = "https://te.legra.ph/file/8c5b5e17d0fba139884d2.jpg"

@Client.on_message(
      filters.command("gender")
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def gender(_, message: Message):
   user = await _.get_me()
   mention = user["mention"]
   await _.send_photo(
      message.chat.id,
      photo,
      caption=Keshav.GENDER.format(message.from_user.mention),
      reply_markup=InlineKeyboardMarkup(Keshav.gender_button))


@Client.on_message(
      filters.command("gender@nothehe_bot")
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def gendero(_, message: Message):
   user = await _.get_me()
   mention = user["mention"]
   await _.send_photo(
      message.chat.id,
      photo,
      caption=Keshav.GENDER.format(message.from_user.mention),
      reply_markup=InlineKeyboardMarkup(Keshav.gender_button))

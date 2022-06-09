from pyrogram.types import InlineKeyboardButton


class AlphaIsAlone:

    cousin_markup = [
          [
          InlineKeyboardButton(text=" ✅ ", callback_data="addc"),
          InlineKeyboardButton(text=" ❌ ", callback_data="deny")
          ]
    ]

    gender_markup = [
          [
          InlineKeyboardButton(" Male 👦 ", callback_data="male"),
          InlineKeyboardButton(" Female 👧 ", callback_data="female")
          ]
    ]

    set_gender_markup = [
          [
          InlineKeyboardButton("Set Gender", url="t.me/nothehe_bot")
          ]
    ]

from pyrogram.types import InlineKeyboardButton


class AlphaIsAlone:

    #tara msg
    TARA = """
💗{} wants to kiss {}...
"""

    #tara buttons
    tara_buttons = [ 
          [  
          InlineKeyboardButton(" ✅ ", callback_data="tara"),
          InlineKeyboardButton(" ❌ ", callback_data="reject")
          ]
    ]

    #tara accept
    TARAA = """
{} accepted the kiss of {} .
"""

    ADD_COUSIN_MALE = """
{} wants {} as his cousin..
"""

    ADD_COUSIN_FEMALE = """
{} wants {} as her cousin..
"""

    cousin_markup = [
          [
          InlineKeyboardButton(" ✅ ", callback_data="addc"),
          InlineKeyboardButton(" ❌ ", callback_data="deny")
          ]
    ]

    gender_markup = [
          [
          InlineKeyboardButton(" Male 👦 ", callback_data="male"),
          InlineKeyboardButton(" Female 👧 ", callback_data="female")
          ]
    ]

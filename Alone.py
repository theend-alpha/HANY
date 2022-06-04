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

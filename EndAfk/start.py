import time

from pyrogram import filters, Client
from pyrogram.types import Message

from EndAfk import app, boot, botname
from EndAfk.helpers import get_readable_time
from EndAfk import SUDOERS

alpha = "https://te.legra.ph/file/5a8e62a134991d1b57e69.jpg"

@Client.on_message(filters.command(["start"]))
async def on_start(_, message: Message):
    bot_uptime = int(time.time() - boot)
    Uptime = get_readable_time(bot_uptime)
    first_name = message.from_user.first_name
    await message.reply_photo(alpha,
        caption=f"hey {first_name} ! This is End Afk ! \n Nice to see ya here ✨💫! \n\n • Part of The End Network"
    )

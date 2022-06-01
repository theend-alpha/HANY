import time

from pyrogram import filters, Client
from pyrogram.types import Message

from EndAfk import app, boot, botname
from EndAfk.helpers import get_readable_time
from EndAfk import SUDOERS

alpha = "https://te.legra.ph/file/5a8e62a134991d1b57e69.jpg"

photo = "https://te.legra.ph/file/834b1444f48d090886fef.jpg"

@Client.on_message(filters.command(["start"], ["start@EndAfkBot"]))
async def on_start(_, message: Message):
    bot_uptime = int(time.time() - boot)
    Uptime = get_readable_time(bot_uptime)
    await message.reply_photo(alpha,
        caption=f"hey Client ! This is End Afk ! \n Nice to see ya here ✨💫! \n\n • Part of The End Network"
    )


@Client.on_message(filters.command("ping") & filters.user(SUDOERS))
async def ping(_, message: Message):
    bot_uptime = int(time.time() - boot)
    Uptime = get_readable_time(bot_uptime)
    await _.send_message(
       message.chat.id,
       f"End is alive. \n\n Uptime - {Uptime}")

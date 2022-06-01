import time

from pyrogram import filters, Client
from pyrogram.types import Message

from EndAfk import app, boot, botname
from EndAfk.helpers import get_readable_time
from EndAfk import SUDOERS

alpha = "https://te.legra.ph/file/5a8e62a134991d1b57e69.jpg"

photo = "https://te.legra.ph/file/834b1444f48d090886fef.jpg"

@Client.on_message(filters.command(["start"], ["start@EndAfkBot"]) & filters.private)
async def on_start(_, message: Message):
    bot_uptime = int(time.time() - boot)
    global Uptime
    Uptime = get_readable_time(bot_uptime)
    first_name = message.from_user.first_name
    await message.reply_photo(alpha,
        caption=f"hey {first_name} ! This is End Afk ! \n Nice to see ya here ✨💫! \n\n • Part of The End Network"
    )

@Client.on_message(
      filters.command(["start"], ["start@EndAfkBot"])
    & filters.group
    & ~filters.edited
    & ~filters.forwarded
    & ~filters.via_bot
)
async def omfoo(_, message: Message):
   user = await _.get_me()
   mention = user["mention"]
   await _.send_photo(
      message.chat.id,
      photo,
      caption=f"Hey! This is End Afk \n\n • part of The End network !")

@Client.on_message(filters.command("ping") & filters.user(SUDOERS))
async def ping(_, message: Message):
    await _.send_message(
       message.chat.id,
       f"End is alive. \n\n Uptime - {Uptime}")

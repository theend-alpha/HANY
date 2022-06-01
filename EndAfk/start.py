import time

from pyrogram import filters
from pyrogram.types import Message

from EndAfk import app, boot, botname
from EndAfk.helpers import get_readable_time

alpha = "https://te.legra.ph/file/5a8e62a134991d1b57e69.jpg"

@app.on_message(filters.command(["start", "ping"]))
async def on_start(_, message: Message):
    bot_uptime = int(time.time() - boot)
    Uptime = get_readable_time(bot_uptime)
    await message.reply_photo(alpha,
        caption=f"{botname} is alive and working good.\n\nUptime : {Uptime}"
    )

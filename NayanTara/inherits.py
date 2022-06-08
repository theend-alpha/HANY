from typing import Callable
from pyrogram import Client 
from pyrogram.types import Message

def nayantara_cb_users(func: Callable) -> Callable:
    async def alpha(client: Client, message: Message):
        if message.from_user.id in SUDO_USERS:
            return await func(client, message)

    return alpha

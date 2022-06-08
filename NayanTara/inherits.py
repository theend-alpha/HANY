"""from typing import Callable
from pyrogram import Client 
from pyrogram.types import Message
from HANY.mygender import OMFOO

def nayantara_cb_users(func: Callable) -> Callable:
    async def alpha(client: Client, message: Message):
        if query.from_user.id in OMFOO:
            return await func(client, message)

    return alpha"""

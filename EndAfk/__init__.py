import asyncio
import time

from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client

import config

loop = asyncio.get_event_loop()
boot = time.time()

mongo = MongoClient(config.MONGO_DB_URI)
db = mongo.AFK

botid = 0
botname = "@EndAfkBot"

SUDOERS = config.SUDO_USER

app = Client(
    ":EndAFKBot:",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)

import asyncio
import time
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
import Config

mongo = MongoClient(Config.MONGO_DB_URI)
db = mongo.YashuAlpha

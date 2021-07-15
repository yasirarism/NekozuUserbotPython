import logging
import sys
import time
from pyrogram import Client, errors
import logging
from decouple import config

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

StartTime = time.time()

api_id = config("api_id", default=None, cast=int)
api_hash = config("api_hash", default=None)
session = config("session", default=None)
PREFIX = config("PREFIX", default=None)
ALIVE_IMG = config("ALIVE_IMG", default=None)

xo = Client(session, api_id=api_id, api_hash=api_hash)

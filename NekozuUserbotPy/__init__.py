import logging
import sys
import time
from pyrogram import Client, errors
import logging
import os
from NekozuUserbotPy.config import Config

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


StartTime = time.time()

API_ID = Config.api_id
API_HASH = Config.api_hash
SESSION = Config.session
PREFIX = Config.prefix
ALIVE_IMG = Config.alive_img

xo = Client(SESSION, api_id=API_ID, api_hash=API_HASH)

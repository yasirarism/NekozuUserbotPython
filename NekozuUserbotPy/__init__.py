import logging
import sys
import time
from pyrogram import Client, errors
import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

if bool(os.environ.get("ENV", True)):
    from NekozuUserbotPy.config import Config

StartTime = time.time()

api_id = Config.api_id
api_hash = Config.api_hash
session = Config.session
PREFIX = Config.prefix
ALIVE_IMG = Config.alive_img

xo = Client(session, api_id=api_id, api_hash=api_hash)

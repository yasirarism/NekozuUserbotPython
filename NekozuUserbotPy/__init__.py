import logging
import sys
import time
from pyrogram import Client, errors
from dotenv import load_dotenv
import logging
import os

load_dotenv("config.env")

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


StartTime = time.time()

API_ID = int(os.environ.get("api_id") or 0)
API_HASH = str(os.environ.get("api_hash") or None)
SESSION = os.environ.get("session", "")
PREFIX = os.environ.get("prefix")
ALIVE_IMG = os.environ.get("alive_img")

xo = Client(SESSION, api_id=API_ID, api_hash=API_HASH)

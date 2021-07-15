from pyrogram import filters
from pyrogram.errors import FloodWait
from NekozuUserbotPy import xo, PREFIX
import asyncio

@xo.on_message(filters.command("alive", PREFIX) & filters.me)
async def spam(Client, message):
    x = message.text
    y = x.split(" ")
    spam_count = int(y[1])
    spam_text = str(y[2:])
    try:
        while spam_count > 0:
            await xo.send_message(message.chat.id, spam_text)
            spam_count -= 1
    except FloodWait as e:
        await asyncio.sleep(e.x)

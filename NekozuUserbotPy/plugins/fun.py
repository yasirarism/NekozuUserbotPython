import requests
from pyrogram import filters
from pyrogram.types import Message
from NekozuUserbotPy import xo, PREFIX


@xo.on_message(filters.command("meme", PREFIX) & filters.me)
async def meme(_, message: Message):
    meme = r.get("https://meme-api.herokuapp.com/gimme/Animemes/").json()
    image = meme.get("url")
    caption = meme.get("title")
    if not image:
        msg.reply_text("No URL was received from the API!")
        return
    xo.send_photo(meme.chat.id, image, caption=caption)

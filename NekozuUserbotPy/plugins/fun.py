import requests
from pyrogram import filters
from NekozuUserbotPy import xo, PREFIX

r = requests.session()

@xo.on_message(filters.command("meme", PREFIX) & filters.me)
def meme(_, m):
    meme = r.get("https://meme-api.herokuapp.com/gimme/Animemes/").json()
    image = meme.get("url")
    caption = meme.get("title")
    if not image:
        msg.reply_text("No URL was received from the API!")
        return
    xo.send_photo(m.chat.id, image, caption=caption)

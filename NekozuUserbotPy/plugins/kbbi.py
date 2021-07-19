import requests
from pyrogram import filters
from pyrogram.types import Message
from NekozuUserbotPy import xo, PREFIX, XTEAM_API
from NekozuUserbotPy.plugins.brainly import get_text

ses = requests.session()

@xo.on_message(filters.command("kbbi", PREFIX) & filters.me)
async def brainly(_, message: Message):
    query = get_text(message)
    url = "https://kbbi-api-zhirrr.vercel.app/api/kbbi?text="+query
    hasil = ses.get(url).json()
    kbbi = hasil['arti']
    await message.edit("Kata: "+query+"\nArti: "+kbbi)

# Credits NekozuUserbot
# Created By @nekozu
import requests
from pyrogram import filters
from pyrogram.types import Message
from NekozuUserbotPy import xo, PREFIX, XTEAM_API

ses = requests.session()

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@xo.on_message(filters.command("br", PREFIX) & filters.me)
async def brainly(_, message: Message):
    query = get_text(message)
    url = "https://api.xteam.xyz/brainly?soal="+query+"&APIKEY="+XTEAM_API
    hasil = ses.get(url).json()
    brainly = hasil['soal']
    beh = hasil['jawaban']
    await message.edit("*Soal**\n`"+brainly+"`\n\n**Jawaban:**\n"+beh)

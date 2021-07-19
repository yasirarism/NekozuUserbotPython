import requests
from pyrogram import filters
from pyrogram.types import Message
from NekozuUserbotPy import xo, PREFIX

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

@xo.on_message(filters.command("kbbi", PREFIX) & filters.me)
async def kbbi(_, message: Message):
    query = get_text(message)
    url = "https://kbbi-api-zhirrr.vercel.app/api/kbbi?text="+query
    hasil = ses.get(url).json()
    kj = hasil['arti']
    jk = hasil['lema']
    await message.edit("**Lema**\n`"+str([jk])+"`\n\n**Arti:**\n"+str([kj])

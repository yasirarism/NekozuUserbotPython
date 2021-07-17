import os

import aiohttp
from aiohttp import ClientResponseError, ServerTimeoutError, TooManyRedirects
from pyrogram import filters
from pyrogram.types import Message
from NekozuUserbotPy import PREFIX, xo

DOGBIN_URL = "https://del.dog/"
NEKOBIN_URL = "https://nekobin.com/"
DOWN_PATH = "./NekozuUserbotPy/"

@xo.on_message(filters.command("paste", PREFIX) & filters.me)
async def paste_(message: Message) -> None:
    await message.edit("`sabar...`")
    text = message.filtered_input_str
    replied = message.reply_to_message
    use_neko = False
    file_ext = '.txt'
    if not text and replied and replied.document and replied.document.file_size < 2 ** 20 * 10:
        file_ext = os.path.splitext(replied.document.file_name)[1]
        path = await replied.download(DOWN_PATH)
        with open(path, 'r') as d_f:
            text = d_f.read()
        os.remove(path)
    elif not text and replied and replied.text:
        text = replied.text
    if not text:
        await message.err("input tidak ditemukan!")
        return
    flags = list(message.flags)
    if 'n' in flags:
        use_neko = True
        flags.remove('n')
    if flags and len(flags) == 1:
        file_ext = '.' + flags[0]
    await message.edit("`Pasting text ...`")
    async with aiohttp.ClientSession() as ses:
        if use_neko:
            async with ses.post(NEKOBIN_URL + "api/documents", json={"content": text}) as resp:
                if resp.status == 201:
                    response = await resp.json()
                    key = response['result']['key']
                    final_url = NEKOBIN_URL + key + file_ext
                    reply_text = f"__Nekobin__ [URL]({final_url})"
                    await message.edit(reply_text, disable_web_page_preview=True)
                else:
                    await message.edit("`Gagal mengcopy ke nekobinn`", del_in=5)
        else:
            async with ses.post(DOGBIN_URL + "documents", data=text.encode('utf-8')) as resp:
                if resp.status == 200:
                    response = await resp.json()
                    key = response['key']
                    final_url = DOGBIN_URL + key
                    if response['isUrl']:
                        reply_text = (f"**PENDEK** [URL]({final_url})\n"
                                      f"**Dogbin** [URL]({DOGBIN_URL}v/{key})")
                    else:
                        reply_text = f"**Dogbin** [URL]({final_url}{file_ext})"
                    await message.edit(reply_text, disable_web_page_preview=True)
                else:
                    await message.edit("`Ggal ke dogbin`", del_in=5)

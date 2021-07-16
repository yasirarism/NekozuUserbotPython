from googletrans import Translator
from pyrogram import filters

from nana import xo, PREFIX

trl = Translator()

@xo.on_message(filters.command("tr", PREFIX) & filters.me)
async def translate(_client, message):
    if message.reply_to_message and (message.reply_to_message.text or message.reply_to_message.caption):
        if len(message.text.split()) == 1:
            await message.edit("Pemakaian: Balas pesan, lalu `tr <bahasa>`")
            return
        target = message.text.split()[1]
        if message.reply_to_message.text:
            text = message.reply_to_message.text
        else:
            text = message.reply_to_message.caption
        detectlang = trl.detect(text)
        try:
            tekstr = trl.translate(text, dest=target)
        except ValueError as err:
            await message.edit("Kesalahan: `{}`".format(str(err)))
            return
        await message.edit("Diterjemahkan dari `{}` to `{}`:\n```{}```".format(detectlang.lang, target, tekstr.text))
    else:
        if len(message.text.split()) <= 2:
            await message.edit("Penggunaan: `tr <bahasa> <teks>`")
            return
        target = message.text.split(None, 2)[1]
        text = message.text.split(None, 2)[2]
        detectlang = trl.detect(text)
        try:
            tekstr = trl.translate(text, dest=target)
        except ValueError as err:
            await message.edit("Error: `{}`".format(str(err)))
            return
        await message.edit("Diterjemahkan dari `{}` ke `{}`:\n```{}```".format(detectlang.lang, target, tekstr.text))

import os

from pyrogram import filters
from telegraph import upload_file

from NekozuUserbotPy import xo, PREFIX

@xo.on_message(filters.command("telegraph", PREFIX) & filters.me)
async def telegraph(client, message):
    replied = message.reply_to_message
    if not replied:
        await message.edit("Reply Ke Media")
        return
    if not ((replied.photo and replied.photo.file_size <= 5242880)
            or (replied.animation and replied.animation.file_size <= 5242880)
            or (replied.video and replied.video.file_name.endswith('.mp4')
                and replied.video.file_size <= 5242880)
            or (replied.document
                and replied.document.file_name.endswith(
                    ('.jpg', '.jpeg', '.png', '.gif', '.mp4'))
                and replied.document.file_size <= 5242880)):
        await message.edit("not supported!")
        return
    download_location = await client.download_media(message=message.reply_to_message,file_name='root/NekozuUserbotPy/')
    await message.edit("`Posting Ke Telegraph...`")
    try:
        response = upload_file(download_location)
    except Exception as document:
        await message.edit(document)
    else:
        await message.edit(f"**Diposting Ke Telegraph: [Telegra.ph](https://telegra.ph{response[0]})**")
    finally:
        os.remove(download_location)

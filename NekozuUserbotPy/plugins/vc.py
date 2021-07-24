# credits plugins https://github.com/xditya/VCBot

from pyrogram import Client, filters
from os import remove
import youtube_dl
from youtube_search import YoutubeSearch
import requests
from NekozuUserbotPy import xo, PREFIX, pycalls, pytgcalls

async def play_a_song(pycalls, message, song):
    try:
        await pycalls.stream(message.chat.id, song)
    except Exception as e:
        await message.edit(f"Error:\n{e}")

@xo.on_message(filters.command("play", PREFIX) & filters.me)
async def stream(_, message):
    txt = message.text.split(" ", 1)
    type_ = None
    try:
        song_name = txt[1]
        type_ = "url"
    except IndexError:
        reply = message.reply_to_message
        if reply:
            if reply.audio:
                med = reply.audio
            elif reply.video:
                med = reply.video
            elif reply.voice:
                med = reply.voice
            else:
                return await message.edit("Balas file audio atau gunakan tautan youtube untuk memutarnya!")
            song_name = med.file_name
            type_ = "tg"
    if type_ == "url":
        if "youtube" not in song_name and "youtu.be" not in song_name:
            return await message.edit("Tidak disupport")
        await message.edit("Dimulai dari `{}`".format(song_name))
        await play_a_song(pycalls, message, song_name)
    elif type_ == "tg":
        x = await message.edit("Mendownload")
        file_ = await reply.download()
        await x.edit("`Memulai...`")
        await play_a_song(pycalls, message, file_)
        remove(file_)
    else:
        return await message.edit("Balas file audio atau gunakan tautan youtube untuk memutarnya!")
      
@xo.on_message(filters.command("pause", PREFIX) & filters.me)
async def pause(_, message):
    pycalls.pause(message.chat.id)
    await message.edit("Berhenti")

@xo.on_message(filters.command("resume", PREFIX) & filters.me)
async def resume(_, message):
    pycalls.resume(message.chat.id)
    await message.edit("Dimulai ulang.")

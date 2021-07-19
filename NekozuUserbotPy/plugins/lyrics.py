import os
import re

import requests
from bs4 import BeautifulSoup
from googlesearch import search
from pyrogram import filters
from pyrogram.types import Message

from NekozuUserbotPy import xo, PREFIX

@xo.on_message(filters.command("lyrics", PREFIX) & filters.me)
async def lyrics(message: Message):
    song = message.input_str
    if not song:
        await message.edit("Bruh WTF?")
        return
    await message.edit(f"__Mencari Lirik {song}__")
    to_search = song + "genius lyrics"
    gen_surl = list(search(to_search, num=1, stop=1))[0]
    gen_page = requests.get(gen_surl)
    scp = BeautifulSoup(gen_page.text, 'html.parser')
    lyrics = scp.find("div", class_="lyrics")
    if not lyrics:
        await message.edit(f"Tidak Ditemukan Untuk: `{song}`")
        return
    lyrics = lyrics.get_text()
    lyrics = re.sub(r'[\(\[].*?[\)\]]', '', lyrics)
    lyrics = os.linesep.join((s for s in lyrics.splitlines() if s))
    title = scp.find('title').get_text().split("|")
    writers_box = [
        writer
        for writer in scp.find_all("span", {'class': 'metadata_unit-label'})
        if writer.text == "Written By"]
    if writers_box:
        target_node = writers_box[0].find_next_sibling("span", {'class': 'metadata_unit-info'})
        writers = target_node.text.strip()
    else:
        writers = "UNKNOWN"
    lyr_format = ''
    lyr_format += '**' + title[0] + '**\n'
    lyr_format += '__' + lyrics + '__'
    lyr_format += "\n\n**Ditulis Oleh: **" + '__' + writers + '__'
    lyr_format += "\n**Sumber: **" + '`' + title[1] + '`'

    if lyr_format:
        await message.edit(lyr_format)
    else:
        await message.edit(f"Tidak ada lirik ditemukan untuk **{song}**")

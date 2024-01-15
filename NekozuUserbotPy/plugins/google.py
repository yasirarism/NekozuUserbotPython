# Credit Usege team https://github.com/usergeteam/userge
import re
import urllib
import urllib.parse
from pyrogram import filters
from pyrogram.types import Message
from fake_useragent import UserAgent

import requests
from bs4 import BeautifulSoup
from NekozuUserbotPy import PREFIX, xo

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None

@xo.on_message(filters.command("google", PREFIX) & filters.me)
async def gsrch(_, message: Message):
    pablo = await message.edit("`Processing..`")
    query = get_text(message)
    if not query:
        await message.edit(
            "`Tolong Beri Saya Masukan yang Valid. Anda Dapat Memeriksa Menu Bantuan Untuk Mengetahui Lebih Lanjut!`"
        )
        return
    query = urllib.parse.quote_plus(query)
    number_result = 8
    ua = UserAgent()
    google_url = f"https://www.google.com/search?q={query}&num={number_result}"
    response = requests.get(google_url, {"User-Agent": ua.random})
    soup = BeautifulSoup(response.text, "html.parser")
    result_div = soup.find_all("div", attrs={"class": "ZINbbc"})
    links = []
    titles = []
    descriptions = []
    for r in result_div:
        try:
            link = r.find("a", href=True)
            title = r.find("div", attrs={"class": "vvjwJb"}).get_text()
            description = r.find("div", attrs={"class": "s3v9rd"}).get_text()
            if link != "" and title != "" and description != "":
                links.append(link["href"])
                titles.append(title)
                descriptions.append(description)

        except:
            continue
    to_remove = []
    clean_links = []
    for i, l in enumerate(links):
        clean = re.search("\/url\?q\=(.*)\&sa", l)
        if clean is None:
            to_remove.append(i)
            continue
        clean_links.append(clean.group(1))
    for x in to_remove:
        del titles[x]
        del descriptions[x]
    msg = "".join(
        f"[{tt}]({liek})\n`{d}`\n\n"
        for tt, liek, d in zip(titles, clean_links, descriptions)
    )
    await message.edit("**Pencarian:**\n`" + query + "`\n\n**Hasil:**\n" + msg)

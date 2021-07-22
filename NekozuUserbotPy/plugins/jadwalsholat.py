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

@xo.on_message(filters.command("jadwalsholat", PREFIX) & filters.me)
async def sholat(_, message: Message):
    query = get_text(message)
    url = "https://pencarikode.xyz/api/sholat?kota="+query+"&apikey=APIKEY"
    hasil = ses.get(url).json()
    kota = hasil['data']['kota']
    tanggal = hasil['data']['tanggal']
    imsak = hasil['data']['imsak']
    terbit = hasil['data']['terbit']
    subuh = hasil['data']['subuh']
    dhuha = hasil['data']['dhuha']
    dzuhur = hasil['data']['dzuhur']
    ashar = hasil['data']['ashar']
    maghrib = hasil['data']['maghrib']
    isya = hasil['data']['isya']
    await message.edit('Kota: '+kota+'\nTanggal: '+tanggal+'\nImsak: '+imsak+'\nTerbit: '+terbit+'\nSubuh: '+subuh+'\nDhuha: '+dhuha+'\nDzuhur: '+dzuhur+'\nAshar: '+ashar+'\nMaghrib: '+maghrib+'\nIsya: '+isya)


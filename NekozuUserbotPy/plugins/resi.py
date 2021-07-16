import requests
from pyrogram import filters

from NekozuUserbotPy import xo, PREFIX

# Credit Arya Hikari And Nana Userbot

@xo.on_message(filters.command("cekresi", PREFIX) & filters.me)
async def resi(_, message):
    msg = message.command
    result = await cek_resi(msg[1], msg[2])
    if msg[1] == 'pos':
        parsed_result = await parse_pos(result)
    else:
        parsed_result = str(result)
    await message.edit("{}".format(parsed_result))
    return


async def cek_resi(courier, awb):
    URL = "https://api.binderbyte.com/cekresi?awb={}&api_key=8e49f28e0f2f2cf56393c352613eec358e85fb7077ce6f7f453ebb826a7b1f6d&courier={}".format(awb, courier)
    r = requests.get(url=URL)
    return r.json()


async def parse_pos(r):
    if r["result"]:
        msg = r['message']
        no_resi = r['data']['waybill']
        ekspedisi = r['data']['courier']
        tracking = r['data']['tracking']
        hasil_track = ""
        for i in tracking:
            hasil_track += await track_pos(i)
        result = f"💬 : {msg} \n\n" \
                 f"📄 : {no_resi} \n" \
                 f"📦 : {ekspedisi} \n\n" \
                 f"📝 Hasil Pelacakan : \n\n" \
                 f"`{hasil_track}`"
    else:
        result = "No Resi Tidak Ditemukan !"
    return result


ktr_tujuan = ""


async def track_pos(tr):
    desc = tr['desc'].split(';')
    detail = ""
    global ktr_tujuan
    if 'LAYANAN' in desc[0]:
        for i in desc:
            detail += f'{i}\n'
    elif 'NO. DO' in desc[0]:
        detail = "Proses Antar Ke alamat Tujuan"
    elif 'KANTOR TUJUAN' in desc[2]:
        detail = f'diteruskan ke :{desc[2]}'
        ktr_tujuan = desc[2].replace('KANTOR TUJUAN :', '')
    elif 'KANTOR ASAL' in desc[2]:
        detail = f'Tiba Di :{ktr_tujuan}'
    elif 'STATUS' in desc[1]:
        detail = f'{desc[1]} \n {desc[2]}'
    print(desc)
    return f"🕔 : {tr['date']}\n" \
           f"📍 : {detail}\n\n"

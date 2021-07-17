import asyncio
from pyrogram import filters
from NekozuUserbotPy import xo, PREFIX


mainhelptext = f"""
You UserBot Is Already Here
Ini Adalah Bantuan
  .adminhelp -> tunjukkan bantuan untuk hal-hal admin.
  .mischelp -> menu random
"""


@xo.on_message(filters.command("help", PREFIX) & filters.me)
def mainhelp(_, m):
    m.edit(mainhelptext)


adminhelptext = f"""
Admin Menu
  .ban -> Blokir pengguna tanpa batas waktu.
  .unban -> Batalkan pemblokiran pengguna.
  .mute -> Membisukan pengguna tanpa batas.
  .unmute -> Suarakan pengguna.
  .kick -> Mengeluarkan pengguna dari grup.
  .pin -> menyematkan pesan.
  .del -> hapus pesan.
  .purge -> bersihkan pesan
"""

@xo.on_message(filters.command("adminhelp", PREFIX) & filters.me)
def mainhelp(_, m):
    m.edit(adminhelptext)

misc = f"""
Misc Menu
  .google -> Mencari Jawaban Digoofle.
  .paste -> Mengcopy pesan ke nekobin.
  .tr (bahasa) -> translate bahasa.
  .ping cek kecepatan bot
  .br -> mencari jawban dibrainly
  .meme -> random animeme
"""

@xo.on_message(filters.command("mischelp", PREFIX) & filters.me)
def mainhelp(_, m):
    m.edit(misc)


import asyncio
from pyrogram import filters
from NekozuUserbotPy import xo, PREFIX


mainhelptext = f"""
You UserBot Is Already Here
Ini Adalah Bantuan
  (prefix)adminhelp -> tunjukkan bantuan untuk hal-hal admin.
"""


@xo.on_message(filters.command("help", PREFIX) & filters.me)
def mainhelp(_, m):
    m.edit(mainhelptext)


adminhelptext = f"""
Admin Menu
  (prefix)ban -> Blokir pengguna tanpa batas waktu.
  (prefix)unban -> Batalkan pemblokiran pengguna.
  (prefix)mute -> Membisukan pengguna tanpa batas.
  (prefix)unmute -> Suarakan pengguna.
  (prefix)kick -> Mengeluarkan pengguna dari grup.
  (prefix)pin -> menyematkan pesan.
  (prefix)del -> hapus pesan.
  (prefix)purge -> bersihkan pesan
"""

@xo.on_message(filters.command("adminhelp", PREFIX) & filters.me)
def mainhelp(_, m):
    m.edit(adminhelptext)
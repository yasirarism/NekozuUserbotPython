import asyncio
from pyrogram import filters
from NekozuUserbotPy import xo, PREFIX


mainhelptext = f"""
You UserBot Is Already Here
Ini Adalah Bantuan
  .adminhelp -> tunjukkan bantuan untuk hal-hal admin.
  .mischelp -> menu random
  .vchelp -> bantuan tentang voice chat
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
  .google -> Mencari Jawaban Digoogle.
  .telegraph -> memposting gambar gif video ke telegraph
  .ping cek kecepatan bot
  .br -> mencari jawaban dibrainly
  .meme -> random animeme
  .gitstalk -> fitur stalk akun github
  .jadwalsholat -> untuk melihatjadwal sholat
  .song -> mencari lagu
"""

@xo.on_message(filters.command("mischelp", PREFIX) & filters.me)
def mainhelp(_, m):
    m.edit(misc)

vc = f"""
Voice Chat
.play (reply ke auudio atau pakai link)
.resume
.pause

"""

@xo.on_message(filters.command("vchelp", PREFIX) & filters.me)
def mainhelp(_, m):
    m.edit(vc)

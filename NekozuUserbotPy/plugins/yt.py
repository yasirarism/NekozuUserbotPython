from youtube_search import YoutubeSearch
import requests
from pyrogram import filters

from NekozuUserbotPy import xo, PREFIX

@xo.on_message(filters.command("song", PREFIX) & filters.me)
def song(_, message):
    query = "".join(" " + str(i) for i in message.command[1:])
    print(query)
    m = message.reply("`Mencari...`")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while not results and count < 6:
            if count > 0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]

            views = results[0]["views"]
            thumb_name = f"thumb{message.message_id}.jpg"
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, "wb").write(thumb.content)

        except Exception as e:
            print(e)
            m.edit("Kosong.")
            return
    except Exception as e:
        m.edit(
            "Tidak ditemukan apapun maaf.."
        )
        print(str(e))
        return
    m.edit("Mendownload.")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"🎧 **Judul**: [{title[:35]}]({link})\n⏳ **Durasi**: `{duration}`\n👁‍🗨 **Penonton**: `{views}`"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(dur_arr[i]) * secmul
            secmul *= 60
        message.reply_audio(
            audio_file,
            caption=rep,
            parse_mode="md",
            quote=False,
            title=title,
            duration=dur,
            thumb=thumb_name,
        )
        m.delete()
    except Exception as e:
        m.edit("❌ Error")
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

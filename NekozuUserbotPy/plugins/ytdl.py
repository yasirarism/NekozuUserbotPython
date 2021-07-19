from pytube import YouTube, exceptions
import requests
from pyrogram import filters
from NekozuUserbotPy import xo, PREFIX

@xo.on_message(filters.command("ytv", PREFIX) & filters.me)
def video_dl(client, message):
    chat_id = message.chat.id
    link = message.text.split(maxsplit=1)[1]
    try:
        yt = YouTube(link)
        video = yt.streams.get_highest_resolution().download('res')
        caption = yt.title
        with open('a.jpg', 'wb') as t:
            t.write(requests.get(yt.thumbnail_url).content)
        thumb = open('a.jpg', 'rb')
        app.send_chat_action(chat_id, "upload_video")
        client.send_video(chat_id=chat_id, video=video, caption=caption,
                          thumb=thumb, duration=yt.length)
        if os.path.exists(video):
            os.remove(video)
        if os.path.exists('a.jpg'):
            os.remove('a.jpg')

    except exceptions.RegexMatchError:
        message.reply_text("URL tidak valid")
    except exceptions.LiveStreamError:
        message.reply_text("Tidak support livestream.")
    except exceptions.VideoUnavailable:
        message.reply_text("Video tidak tersedia.")
    except exceptions.HTMLParseError:
        message.reply_text("Url Salah.")

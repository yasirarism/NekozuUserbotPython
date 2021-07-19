import aiohttp
from pyrogram import filters
from NekozuUserbotPy import xo, PREFIX

@xo.on_message(filters.command("gitstalk", PREFIX) & filters.me)
@capture_err
async def github(_, message):
    if len(message.command) != 2:
        await message.reply_text("/gitstalk Username")
        return
    username = message.text.split(None, 1)[1]
    URL = f'https://api.github.com/users/{username}'
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as request:
            if request.status == 404:
                return await message.reply_text("404")

            result = await request.json()
            try:
                url = result['html_url']
                name = result['name']
                company = result['company']
                bio = result['bio']
                created_at = result['created_at']
                avatar_url = result['avatar_url']
                blog = result['blog']
                location = result['location']
                repositories = result['public_repos']
                followers = result['followers']
                following = result['following']
                caption = f"""**Info Of {name}**
**Username:** `{username}`
**Bio:** `{bio}`
**Profil Link:** [Here]({url})
**Perusahaan:** `{company}`
**Dibuat pada:** `{created_at}`
**Repositories:** `{repositories}`
**Blog:** `{blog}`
**Lokasi:** `{location}`
**Followers:** `{followers}`
**Following:** `{following}`"""
            except Exception as e:
                print(str(e))
                pass
    await message.reply_photo(photo=avatar_url, caption=caption)

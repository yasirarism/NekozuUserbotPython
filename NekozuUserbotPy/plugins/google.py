# Credit userge 

from search_engine_parser.core.engines.google import Search as GoogleSearch
from pyrogram.types import Message
from NekozuUserbotPy import xo, PREFIX

@xo.on_message(filters.command("google", PREFIX) & filters.me)
async def gsearch(message: Message):
    await message.edit("Proses ...")
    query = message.filtered_input_str
    flags = message.flags
    page = int(flags.get("-p", 1))
    limit = int(flags.get("-l", 5))
    if message.reply_to_message:
        query = message.reply_to_message.text
    if not query:
        await message.err(text="Berikan pertanyaan atau balas pesan!")
        return
    try:
        g_search = GoogleSearch()
        gresults = await g_search.async_search(query, page)
    except Exception as e:
        await message.err(text=e)
        return
    output = ""
    for i in range(limit):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            output += f"[{title}]({link})\n"
            output += f"`{desc}`\n\n"
        except IndexError:
            break
    output = f"**Pencarian Google:**\n`{query}`\n\n**Hasil:**\n{output}"
    await message.edit_or_send_as_file(
        text=output, caption=query, disable_web_page_preview=True
    )

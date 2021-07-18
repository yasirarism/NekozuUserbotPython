import wikipedia

from pyrogram import filters
from pyrogram.types import Message
from NekozuUserbotPy import xo, PREFIX

@xo.on_message(filters.command("wiki", PREFIX) & filters.me)
async def wiki(_, message: Message):
    await message.edit("__Mencari__ ...")
    query = message.filtered_input_str
    flags = message.flags
    limit = int(flags.get('-l', 5))
    if message.reply_to_message:
        query = message.reply_to_message.text
    if not query:
        await message.err(text="`Kasih kata kunci pencarian`!")
        return
    try:
        wikipedia.set_lang("en")
        results = wikipedia.search(query)
    except Exception as e:
        await message.err(e)
        return
    output = ""
    for i, s in enumerate(results, start=1):
        page = wikipedia.page(s)
        url = page.url
        output += f" [{s}]({url})\n"
        if i == limit:
            break
    output = f"**Pencarian:**\n`{query}`\n\n**Hasil:**\n{output}"
    await message.edit_or_send_as_file(text=output, caption=query,
                                       disable_web_page_preview=True)

import asyncio

from pyrogram import filters
from pyrogram.methods.chats.get_chat_members import Filters as ChatMemberFilters
from pyrogram.types import Message

from NekozuUserbotPy import xo, PREFIX


@app.on_message(filters.command("pin", PREFIX) & filters.me)
async def pin_message(_, message: Message):
    if message.chat.type in ["group", "supergroup"]:
        # Here lies the sanity checks
        admins = await app.get_chat_members(
            message.chat.id, filter=ChatMemberFilters.ADMINISTRATORS
        )
        admin_ids = [user.user.id for user in admins]
        me = await app.get_me()

        # If you are an admin
        if me.id in admin_ids:
            # If you replied to a message so that we can pin it.
            if message.reply_to_message:
                disable_notification = True

                # Let me see if you want to notify everyone. People are gonna hate you for this...
                if len(message.command) >= 2 and message.command[1] in [
                    "alert",
                    "notify",
                    "loud",
                ]:
                    disable_notification = False

                await app.pin_chat_message(
                    message.chat.id,
                    message.reply_to_message.message_id,
                    disable_notification=disable_notification,
                )
                await message.edit("__DiPin!__")
            else:
                # You didn't reply to a message and we can't pin anything. ffs
                await message.edit(
                    "`Balas pesan agar aku bisa menyematkan benda terkutuk itu...`"
                )
        else:
            # You have no business running this command.
            await message.edit("**aku bukan admin di sini. Apa yang harus aku lakukan?**")
    else:
        # Are you fucking dumb this is not a group ffs.
        await message.edit("`Bagaimana cara pin pesan ?.`")

    # And of course delete your lame attempt at changing the group picture.
    # RIP you.
    # You're probably gonna get ridiculed by everyone in the group for your failed attempt.
    # RIP.
    await asyncio.sleep(3)
    await message.delete()

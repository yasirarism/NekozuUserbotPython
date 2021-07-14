import time
from pyrogram import filters
from pyrogram.types import Message, ChatPermissions

from pyrogram.errors import UserAdminInvalid

from NekozuUserbotPy import xo
from NekozuUserbotPy import xo as app
from NekozuUserbotPy.helpers.pyro import GetUserMentionable
from NekozuUserbotPy.helpers.admem import CheckAdmin, CheckReplyAdmin, RestrictFailed
from NekozuUserbotPy import PREFIX

@xo.on_message(filters.command("ban", PREFIX) & filters.me)
async def ban_hammer(_, message: Message):
    if await CheckReplyAdmin(message) is True and await CheckAdmin(message) is True:
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)
            if message.command == ["ban", "24"]:
                await app.kick_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.reply_to_message.from_user.id,
                    until_date=int(time.time() + 86400),
                )
                await message.edit(f"{mention} telah dibanned selama 24 jam.")
            else:
                await app.kick_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.reply_to_message.from_user.id,
                )
                await message.edit(f"{mention} telah dibanned tanpa batas waktu.")
        except UserAdminInvalid:
            await RestrictFailed(message)


@xo.on_message(filters.command("unban", PREFIX) & filters.me)
async def unban(_, message: Message):
    if await CheckReplyAdmin(message) is True and await CheckAdmin(message) is True:
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)
            await app.unban_chat_member(
                chat_id=message.chat.id, user_id=message.reply_to_message.from_user.id
            )
            await message.edit(f"{mention} sudah tidak dibanned.")
        except UserAdminInvalid:
            await message.edit("Mengmaaf, Aku tidak dapat membatalkan pemblokiran pengguna ini.")


# Mute Permissions
mute_permission = ChatPermissions(
    can_send_messages=False,
    can_send_media_messages=False,
    can_send_stickers=False,
    can_send_animations=False,
    can_send_games=False,
    can_use_inline_bots=False,
    can_add_web_page_previews=False,
    can_send_polls=False,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@xo.on_message(filters.command(["mute", "mute 24"], ".") & filters.me)
async def mute_hammer(_, message: Message):
    if await CheckReplyAdmin(message) is True and await CheckAdmin(message) is True:
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)
            if message.command == ["mute", "24"]:
                await app.restrict_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.reply_to_message.from_user.id,
                    permissions=mute_permission,
                    until_date=int(time.time() + 86400),
                )
                await message.edit(f"{mention} telah dibisukan selama 24 jam.")
            else:
                await app.restrict_chat_member(
                    chat_id=message.chat.id,
                    user_id=message.reply_to_message.from_user.id,
                    permissions=mute_permission,
                )
                await message.edit(f"{mention} telah dibisukan tanpa batas waktu.")
        except UserAdminInvalid:
            await RestrictFailed(message)


# Unmute permissions
unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_stickers=True,
    can_send_animations=True,
    can_send_games=True,
    can_use_inline_bots=True,
    can_add_web_page_previews=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@xo.on_message(filters.command("unmute", PREFIX) & filters.me)
async def unmute(_, message: Message):
    if await CheckReplyAdmin(message) is True and await CheckAdmin(message) is True:
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)
            await app.restrict_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
                permissions=unmute_permissions,
            )
            await message.edit(f"{mention}, telah tidak dibisukan.")
        except UserAdminInvalid:
            await RestrictFailed(message)


@xo.on_message(filters.command("kick", PREFIX) & filters.me)
async def kick_user(_, message: Message):
    if await CheckReplyAdmin(message) is True and await CheckAdmin(message) is True:
        try:
            mention = GetUserMentionable(message.reply_to_message.from_user)
            await app.kick_chat_member(
                chat_id=message.chat.id,
                user_id=message.reply_to_message.from_user.id,
            )
            await message.edit(f"{mention}, Ditendang!.")
        except UserAdminInvalid:
            await RestrictFailed(message)

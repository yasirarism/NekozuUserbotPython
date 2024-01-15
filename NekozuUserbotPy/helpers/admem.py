from time import sleep, time

from pyrogram.types import Message

from NekozuUserbotPy import xo
from NekozuUserbotPy.helpers.interval import IntervalHelper


async def CheckAdmin(message: Message):
    admin = "administrator"
    creator = "creator"
    ranks = [admin, creator]

    SELF = await xo.get_chat_member(
        chat_id=message.chat.id, user_id=message.from_user.id
    )

    if SELF.status not in ranks:
        await message.edit("__I'm not Admin!__")
    elif SELF.status is not admin or SELF.can_restrict_members:
        return True
    else:
        await message.edit("__No Permissions to restrict Members__")
    sleep(2)
    await message.delete()


async def CheckReplyAdmin(message: Message):
    """Check if the message is a reply to another user."""
    if not message.reply_to_message:
        await message.edit(f"`.{message.command[0]}` needs to be a reply")
        sleep(2)
        await message.delete()
    elif message.reply_to_message.from_user.is_self:
        await message.edit(f"I can't {message.command[0]} myself.")
        sleep(2)
        await message.delete()
    else:
        return True


async def Timer(message: Message):
    if len(message.command) <= 1:
        return 0
    secs = IntervalHelper(message.command[1])
    return int(str(time()).split(".")[0] + secs.to_secs()[0])


async def TimerString(message: Message):
    secs = IntervalHelper(message.command[1])
    return f"{secs.to_secs()[1]} {secs.to_secs()[2]}"


async def RestrictFailed(message: Message):
    await message.edit(f"I can't {message.command} this user.")
    sleep(2)
    await message.delete()

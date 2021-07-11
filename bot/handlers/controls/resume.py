from pyrogram.types import Message

from ... import server
from .. import group_command


@group_command("resume", "r")
async def _(_, message: Message):
    result = await server.resume(message.chat.id)

    if result:
        await message.reply_text("<b>▶️ Resumed</b>", False)
    elif result == False:
        await message.reply_text("<b>❌ Nothing is paused</b>", False)
    else:
        await message.reply_text("<b>❌ Not in call</b>", False)

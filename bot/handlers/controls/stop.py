from pyrogram.types import Message

from ... import server
from .. import group_command


@group_command("stop")
async def _(_, message: Message):
    result = await server.stop(message.chat.id)

    if result:
        await message.reply_text("<b>⏹ Stopped</b>", False)
    else:
        await message.reply_text("<b>❌ Not in call</b>", False)

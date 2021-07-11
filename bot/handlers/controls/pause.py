from pyrogram.types import Message

from ... import server
from .. import group_command


@group_command("pause", "p")
async def _(_, message: Message):
    result = await server.pause(message.chat.id)

    if result:
        await message.reply_text("<b>⏸ Paused</b>", False)
    elif result == False:
        await message.reply_text("<b>❌ Nothing is playing</b>", False)
    else:
        await message.reply_text("<b>❌ Not in call</b>", False)

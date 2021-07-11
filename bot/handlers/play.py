from os import path
from pyrogram.types import Message

from .. import server
from ..helpers.link import create_link
from ..helpers.graphic import create_graphic
from ..helpers.message import send_now_playing, send_queued_at

from . import group_command

audio_files_dir = path.join(path.dirname(__file__), "a")


@group_command("play")
async def _(_, message: Message):
    if message.reply_to_message and (
        message.reply_to_message.audio or message.reply_to_message.voice
    ):
        file = path.join(
            audio_files_dir,
            (
                message.reply_to_message.audio or message.reply_to_message.voice
            ).file_unique_id,
        )

        if not path.isfile(file):
            await message.reply_to_message.download(file)

        requester = message.from_user.mention()
        link = create_link(
            message.reply_to_message.link,
            message.reply_to_message.audio.title or "an audio file"
            if message.reply_to_message.audio
            else "a voice message",
        )

        result = await server.stream(message.chat.id, file)

        if isinstance(result, int):
            await send_queued_at(
                message,
                create_graphic(message.reply_to_message),
                requester,
                link,
                result,
            )
        else:
            await send_now_playing(
                message,
                create_graphic(message.reply_to_message),
                requester,
                link,
            )

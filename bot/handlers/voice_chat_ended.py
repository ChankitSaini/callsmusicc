from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message

from .. import server


@Client.on_message(filters.voice_chat_ended)
async def _(_, message: Message):
    await server.leave(message.chat.id)

from pyrogram.types import Message

from ..graphics import create_graphic as _create_graphic


def create_graphic(message_with_audio: Message):
    message = message_with_audio

    if message.audio:
        audio = message.audio
        text = "Audio\nFile"

        if audio.title and audio.performer:
            text = audio.performer + "\n" + audio.title
        elif audio.title:
            text = audio.title

        return _create_graphic(text)
    else:
        return _create_graphic("Voice\nMessage")

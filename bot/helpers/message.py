from io import BytesIO
from typing import Union

from pyrogram.types import Message


async def send_queued_at(
    message: Message,
    photo: Union[str, BytesIO],
    requester: str,
    link: str,
    position: int,
):
    await message.reply_photo(
        photo=photo,
        caption=f"<b>#️⃣ {requester} queued {link} at position {position}...</b>",
        quote=False,
    )


async def send_now_playing(
    message: Message,
    photo: Union[str, BytesIO],
    requester: str,
    link: str,
):
    await message.reply_photo(
        photo=photo,
        caption=f"<b>▶️ {requester} is now playing {link}...</b>",
        quote=False,
    )


def get_text_links(message: Message):
    return [
        entity
        for entity in (message.entities or message.caption_entities)
        if entity.type == "text_link"
    ]


def get_minutes(message: Message, result: int) -> int:
    dur = list(
        map(
            int,
            ((message.text or message.caption).split("\n\n"))[result - 1]
            .split("\n")[-1][5:]
            .split(":"),
        ),
    )

    if len(dur) == 3:
        return 99
    elif len(dur) == 2:
        return dur[0]
    else:
        return 0

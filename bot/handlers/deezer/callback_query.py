from pyrogram.types import CallbackQuery

from ... import server
from ... import graphics
from ...downloaders import deezer
from ...helpers.callback import ensure_requester
from ...helpers.link import create_link
from ...helpers.message import send_now_playing, send_queued_at, get_text_links

from .. import callback


@callback("deezer_[1-9]")
async def _(_, query: CallbackQuery):
    if not await ensure_requester(query):
        return

    await query.message.delete()

    track_id = int(
        ((get_text_links(query.message))[int(query.data.split("_")[-1]) - 1]).url.split(
            "/"
        )[-1],
    )

    file, track_info = (await deezer.download(track_id)).values()

    requester = query.message.reply_to_message.from_user.mention()
    photo = await graphics.add_logo(track_info["album"]["cover_xl"])

    link = create_link(
        track_info["link"], f'{track_info["artist"]["name"]} — {track_info["title"]}'
    )

    result = await server.stream(query.message.chat.id, file)

    if isinstance(result, int):
        await send_queued_at(
            query.message,
            photo,
            requester,
            link,
            result,
        )
    else:
        await send_now_playing(
            query.message,
            photo,
            requester,
            link,
        )

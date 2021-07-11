from pyrogram.types import CallbackQuery

from ... import server
from ...downloaders import youtube
from ...helpers.message import (
    send_queued_at,
    send_now_playing,
    get_minutes,
    get_text_links,
)
from ...helpers.link import create_link
from ...helpers.callback import ensure_requester
from ...helpers.bytes import url_to_bytes_io

from .. import callback


@callback("youtube_[1-9]")
async def _(_, query: CallbackQuery):
    if not await ensure_requester(query):
        return

    selected_result = int(query.data.split("_")[-1])

    if get_minutes(query.message, selected_result) > 11:
        await query.answer("❌ Try something shorter", show_alert=True)
        return

    await query.message.delete()

    url = get_text_links(query.message)[selected_result - 1].url

    file, video_info = youtube.download(url)

    graphic = await url_to_bytes_io(video_info["thumbnails"][-1]["url"])
    graphic.name = "thumbnail.png"

    requester = query.message.reply_to_message.from_user.mention()

    link = create_link(f'https://youtu.be/{video_info["id"]}', video_info["title"])

    result = await server.stream(query.message.chat.id, file)

    if isinstance(result, int):
        await send_queued_at(
            query.message,
            graphic,
            requester,
            link,
            result,
        )
    else:
        await send_now_playing(
            query.message,
            graphic,
            requester,
            link,
        )

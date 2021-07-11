from pyrogram import Client
from pyrogram.types import Message

from ... import assets
from ...downloaders import youtube
from ...handlers import group_command
from ...helpers.text import get_youtube_search_results_text
from ...helpers.reply_markup import get_search_results_reply_markup


@group_command("youtube", "yt")
async def _(client: Client, message: Message):
    if len(message.command) == 1:
        await message.reply_text("<b>❓ What do you want to play?</b>")
        return

    results = await youtube.search(" ".join(message.command[1:]))

    if results:
        text = get_youtube_search_results_text(results)
        reply_markup = get_search_results_reply_markup(len(results), "youtube")

        await (
            message.reply_photo(
                photo=assets.get_asset("png", "youtube_search_results"),
                caption=text,
                reply_markup=reply_markup,
            )
            if len((await client.parser.parse(text, "html"))["message"]) <= 1024
            else message.reply_text(
                text=text,
                disable_web_page_preview=True,
                reply_markup=reply_markup,
            )
        )
    else:
        await message.reply_text(
            text="<b>❌ No results found</b>",
            quote=False,
        )

from pyrogram.types import Message

from ...assets import get_asset
from ...downloaders import deezer
from ...helpers.text import get_deezer_search_results_text
from ...helpers.reply_markup import get_search_results_reply_markup

from .. import group_command


@group_command("deezer", "dz")
async def _(_, message: Message):
    if len(message.command) == 1:
        await message.reply_text("<b>❓ What do you want to play?</b>")
        return

    results = await deezer.search(" ".join(message.command[1:]))

    if results:
        await (
            lambda results: message.reply_photo(
                photo=get_asset("png", "deezer_search_results"),
                caption=get_deezer_search_results_text(results),
                reply_markup=get_search_results_reply_markup(len(results), "deezer"),
            )
        )(results)
    else:
        await message.reply_text("<b>❌ No results found</b>")

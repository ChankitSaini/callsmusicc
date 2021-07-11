from pyrogram.types import CallbackQuery

from ..helpers.callback import ensure_requester
from . import callback


@callback("close")
async def _(_, query: CallbackQuery):
    if not await ensure_requester(query):
        return

    await query.answer()
    await query.message.delete()

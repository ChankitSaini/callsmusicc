from pyrogram.types import CallbackQuery


async def ensure_requester(query: CallbackQuery):
    if query.from_user.id != query.message.reply_to_message.from_user.id:
        await query.answer("❌ This is not for you", show_alert=True)
        return False

    return True

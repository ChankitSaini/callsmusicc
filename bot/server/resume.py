from typing import Optional
from .fetcher import fetch
from .helpers import return_result


async def resume(chat_id: int) -> Optional[bool]:
    return return_result(await fetch("resume", {"chatId": chat_id}))

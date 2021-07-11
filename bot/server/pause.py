from typing import Optional
from .fetcher import fetch
from .helpers import return_result


async def pause(chat_id: int) -> Optional[bool]:
    return return_result(await fetch("pause", {"chatId": chat_id}))

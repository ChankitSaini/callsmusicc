from typing import Optional
from .fetcher import fetch
from .helpers import return_result


async def leave(chat_id: int) -> Optional[bool]:
    return return_result(await fetch("leave", {"chatId": chat_id}))

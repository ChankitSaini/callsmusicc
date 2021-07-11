from typing import Optional
from .fetcher import fetch
from .helpers import return_result


async def stop(chat_id: int) -> Optional[bool]:
    return return_result(await fetch("stop", {"chatId": chat_id}))

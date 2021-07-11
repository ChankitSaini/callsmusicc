from typing import Optional
from .fetcher import fetch
from .helpers import return_result


async def stream(chat_id: int, file_path: str) -> Optional[int]:
    return return_result(
        await fetch("stream", {"chatId": chat_id, "filePath": file_path})
    )

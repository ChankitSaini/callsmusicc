from typing import Dict, Union
from httpx import AsyncClient
from ..env import PORT

client = AsyncClient()


async def fetch(method: str, args: Dict[str, Union[str, int]]):
    return (
        await client.get(f"http://127.0.0.1:{PORT}/api/{method}", params=args)
    ).json()

from io import BytesIO

from httpx import AsyncClient

httpx = AsyncClient()


async def url_to_bytes_io(url: str) -> BytesIO:
    return BytesIO((await httpx.get(url)).content)

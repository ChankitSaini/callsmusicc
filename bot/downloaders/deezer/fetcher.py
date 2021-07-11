from httpx import AsyncClient

client = AsyncClient()


async def fetch(url):
    return (await client.get(url)).json()

from urllib.parse import urlencode
from . import fetcher


async def search(query: str, max_results: int = 9):
    return (
        await fetcher.fetch(f"http://api.deezer.com/search?{urlencode({'q': query})}")
    )["data"][:max_results]

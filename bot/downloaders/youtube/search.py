from youtubesearchpython.__future__ import VideosSearch


async def search(query: str, limit: int = 9):
    return (await VideosSearch(query, limit=limit).next())["result"]

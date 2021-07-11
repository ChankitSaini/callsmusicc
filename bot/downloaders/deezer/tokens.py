from . import fetcher


async def get_token():
    return (
        await fetcher.fetch(
            "https://tv.deezer.com/smarttv/8caf9315c1740316053348a24d25afc7/app_access_token.php?device=lg"
        )
    )["access_token"]

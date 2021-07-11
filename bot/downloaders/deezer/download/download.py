from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from .. import tokens, fetcher
from . import md5


async def download(track_id: int):
    return (
        lambda track: {
            "dl": (
                lambda _: (
                    "https://e-cdns-proxy-"
                    + track["md5_origin"][0]
                    + ".dzcdn.net/api/1/"
                    + Cipher(
                        algorithms.AES(b"jo6aey6haid2Teih"),
                        modes.ECB(),
                        backend=default_backend(),
                    )
                    .encryptor()
                    .update(_ + (b"." * (16 - (len(_) % 16))))
                    .hex()
                )
            )(
                (lambda _: md5.md5(_).encode() + b"\xa4" + _ + b"\xa4")(
                    b"\xa4".join(
                        [
                            track["md5_origin"].encode(),
                            "3".encode(),
                            f"{track_id}".encode(),
                            str(track["media_version"]).encode(),
                        ]
                    )
                )
            ),
            "track": track,
        }
    )(
        await fetcher.fetch(
            f"https://api.deezer.com/track/{track_id}?access_token={await tokens.get_token()}"
        )
    )

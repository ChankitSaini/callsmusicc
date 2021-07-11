from io import BytesIO

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from .assets import get_asset
from .helpers.bytes import url_to_bytes_io

logo = Image.open(get_asset("png", "logo"))
font = ImageFont.truetype(get_asset("ttf", "font"), 100)


def create_graphic(text):
    image = Image.open(get_asset("png", "graphic"))
    draw = ImageDraw.Draw(image)
    text = text.split("\n")

    for i in range(len(text)):
        part = text[i].strip().rstrip()

        if len(part) > 20:
            part = part[:18] + ".."

        text[i] = part

    text = "\n".join(text)

    draw.text(
        xy=(
            (image.width - draw.textsize(text, font=font)[0]) / 2,
            293,
        ),
        text=text,
        fill=(255, 255, 255),
        font=font,
    )

    io = BytesIO()
    image.save(io, format="PNG")
    io.name = "thumbnail.png"
    return io


async def add_logo(cover_url: str):
    thumbnail = Image.open(await url_to_bytes_io(cover_url))
    thumbnail.paste(logo, (30, 30), logo)
    io = BytesIO()
    thumbnail.save(io, format="PNG")
    io.name = "thumbnail.png"
    return io

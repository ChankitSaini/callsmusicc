from pyrogram import Client
from pyrogram import filters

from ..env import PREFIXES


def command(*commands):
    return filters.command([*commands], PREFIXES)


def group_command(*commands):
    return Client.on_message(
        command(*commands)
        & filters.group
        & ~filters.edited
        & ~filters.forwarded
        & ~filters.via_bot,
    )


def callback(regex):
    return Client.on_callback_query(filters.regex(regex))

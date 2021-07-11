from os import path
from multiprocessing import Process

from pyrogram import Client
from Naked.toolshed.shell import execute_js

from .constants import ROOT_DIR
from .env import API_ID, API_HASH, BOT_TOKEN

SERVER_DIR = path.join(ROOT_DIR, "server", "dist")


def run_server():
    try:
        execute_js(SERVER_DIR)
    except KeyboardInterrupt:
        pass


client = Client(
    session_name="bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={"root": "bot.handlers"},
)


def start():
    Process(target=run_server).start()
    client.run()

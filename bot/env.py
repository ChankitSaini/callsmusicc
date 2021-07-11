from os import getenv
from dotenv import load_dotenv
from .constants import ROOT_DIR

load_dotenv()

BOT_TOKEN = getenv("BOT_TOKEN")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

PREFIXES = getenv("CMD_PREFIXES", "/ !").split()
PORT = int(getenv("PORT", "8080"))

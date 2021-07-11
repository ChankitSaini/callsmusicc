from os import path
from .constants import ROOT_DIR


def get_asset(type: str, file_name: str):
    return path.join(ROOT_DIR, "assets", type, file_name + "." + type)

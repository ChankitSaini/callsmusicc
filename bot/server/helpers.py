from typing import Any


def return_result(json: Any):
    if json["ok"]:
        return json["result"]

    raise Exception(json["result"])

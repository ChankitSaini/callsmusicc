from typing import List
from ..constants import NUMBER_EMOJIS


def _format_duration(duration: int) -> str:
    result = ""
    remainder = duration
    r_ange_s = {
        "d": (24 * 60 * 60),
        "h": (60 * 60),
        "m": 60,
        "s": 1,
    }

    for age in r_ange_s:
        divisor = r_ange_s[age]
        v_m, remainder = divmod(remainder, divisor)
        v_m = int(v_m)
        if v_m != 0:
            result += f" {v_m}{age} "

    return " ".join(result.split())


def get_deezer_search_results_text(results: List[dict]):
    return "\n\n".join(
        [
            (
                '{number} <b><a href="https://deezer.com/track/{id}">{title}</a></b>\n ├ 👤 {artist}\n └ 🕓 {duration}'
            ).format(
                number=NUMBER_EMOJIS[str(i + 1)]
                if str(
                    i + 1,
                )
                in NUMBER_EMOJIS
                else str(i + 1),
                id=results[i]["id"],
                title=results[i]["title"],
                artist=results[i]["artist"]["name"],
                duration=_format_duration(results[i]["duration"]),
            )
            for i in range(len(results))
        ],
    )


def get_youtube_search_results_text(results: List[dict]):
    return "\n\n".join(
        [
            (
                '{number} <b><a href="{url}">{title}</a></b>\n ├ 👤 {artist}\n └ 🕓 {duration}'
            ).format(
                number=NUMBER_EMOJIS[str(i + 1)]
                if str(
                    i + 1,
                )
                in NUMBER_EMOJIS
                else str(i + 1),
                url=results[i]["link"],
                title=results[i]["title"]
                if len(
                    results[i],
                )
                < 20
                else results[i]["title"][:17] + "...",
                artist=results[i]["channel"]["name"],
                duration=results[i]["duration"],
            )
            for i in range(len(results))
        ],
    )

from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup

from ..constants import NUMBER_EMOJIS


def get_search_results_reply_markup(results: int, callback_data: str):
    buttons = [[]]

    for _ in range(results):
        to_append = (
            lambda _: InlineKeyboardButton(
                text=NUMBER_EMOJIS[_] if _ in NUMBER_EMOJIS else _,
                callback_data=f"{callback_data}_{_}",
            )
        )(str(sum([len(l) for l in buttons]) + 1))
        buttons[-1].append(to_append) if (
            len(buttons[-1])
            in (
                0,
                1,
            )
        ) else buttons.append([to_append])

    return InlineKeyboardMarkup(
        inline_keyboard=(
            [
                *buttons,
                [
                    InlineKeyboardButton(
                        text="🗑 Close",
                        callback_data="close",
                    ),
                ],
            ]
        ),
    )

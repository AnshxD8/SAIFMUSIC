from pyrogram.types import InlineKeyboardButton

import config
from VenomX import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=" 𝐂𝐎𝐃𝐄𝐑 ", url="https://t.me/ANSH_XD8"),
            InlineKeyboardButton(text=" 🇦ηѕн  ", url="https://t.me/ANSH_XDZ"),
        ],
        [
            InlineKeyboardButton(text=" 𝐒𝐔𝐏𝐏𝐎𝐑𝐓  ", url="https://t.me/THE_CASTLESS"),
            InlineKeyboardButton(text="👀 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 👀", url="https://t.me/ANSH_XD8"),
        ],
    ]
    return buttons

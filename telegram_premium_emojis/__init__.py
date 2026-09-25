"""
telegram-premium-emojis
~~~~~~~~~~~~~~~~~~~~~~~
A modern toolkit and AI Agent Skill for implementing Telegram Bot Premium Custom Emojis,
Aiogram 3 card UI, icon_custom_emoji_id inline buttons, and sticker pack discovery.

:copyright: (c) 2026 by Abbos & OsonPDF Open Source Community.
:license: MIT, see LICENSE for more details.
"""

from .constants import CommonIcons, RestrictedIcons, FULL_WIDTH_SPACER, ICON_FALLBACKS
from .builder import TelegramCard, tg_emoji, validation_badge, build_inline_button
from .scanner import scan_pack, fetch_sticker_set
from .validator import validate_file, validate_path

__version__ = "1.0.0"
__all__ = [
    "CommonIcons",
    "RestrictedIcons",
    "FULL_WIDTH_SPACER",

    "ICON_FALLBACKS",
    "TelegramCard",
    "tg_emoji",
    "validation_badge",
    "build_inline_button",
    "scan_pack",
    "fetch_sticker_set",
    "validate_file",
    "validate_path",
]

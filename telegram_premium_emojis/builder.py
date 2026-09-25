"""
Telegram Premium UI Card & Button Builder
"""
from typing import Optional, List
from .constants import FULL_WIDTH_SPACER, CommonIcons, ICON_FALLBACKS


def tg_emoji(emoji_id: str, fallback: Optional[str] = None) -> str:
    """
    Format a Telegram Custom Emoji in HTML parse mode.
    
    Example:
        tg_emoji(CommonIcons.DIAMOND) -> '<tg-emoji emoji-id="5807465992363710697">💎</tg-emoji>'
    """
    fb = fallback or ICON_FALLBACKS.get(emoji_id, "✨")
    return f'<tg-emoji emoji-id="{emoji_id}">{fb}</tg-emoji>'


def validation_badge(level: str, text: str) -> str:
    """
    Create a standardized status or validation line with appropriate custom emoji.
    Levels: 'success', 'error', 'warning', 'info', 'pending'
    """
    level_map = {
        "success": (CommonIcons.SUCCESS, "✅"),
        "error": (CommonIcons.ERROR, "❌"),
        "warning": (CommonIcons.WARNING, "⚠️"),
        "info": (CommonIcons.INFO, "ℹ️"),
        "pending": (CommonIcons.PENDING, "⏳"),
    }
    icon_id, fb = level_map.get(level.lower(), (CommonIcons.INFO, "ℹ️"))
    return f"{tg_emoji(icon_id, fb)} {text}"


class TelegramCard:
    """
    Fluent builder for production-grade Telegram Bot message cards.
    
    Guarantees compliance with Telegram UI/UX standards:
    1. Title: Bold (<b>...</b>) in a regular line OUTSIDE the blockquote.
    2. Body: Italic inside blockquote (<blockquote><i>...</i></blockquote>).
    3. Full-width invisible spacer: prevents awkward narrow blockquotes.
    4. Signature: Optional expandable signature block (<blockquote expandable><i>...</i></blockquote>).
    
    Example:
        card = (
            TelegramCard()
            .set_title("PDF to Word", icon_id=CommonIcons.DOCUMENT)
            .add_line("Convert your PDF documents into editable Word files.", icon_id=CommonIcons.SPARKLES)
            .add_line("Maximum file size: 50 MB", icon_id=CommonIcons.ATTACH)
            .add_line("Preserves tables, images, and formatting", icon_id=CommonIcons.SUCCESS)
            .with_spacer()
            .set_signature("@mybot - Ready in 5 seconds", expandable=True)
            .build()
        )
    """

    def __init__(self):
        self._title: Optional[str] = None
        self._title_icon_id: Optional[str] = None
        self._title_fallback: Optional[str] = None
        self._lines: List[str] = []
        self._use_spacer: bool = True
        self._signature: Optional[str] = None
        self._signature_expandable: bool = True
        self._extra_blocks: List[str] = []

    def set_title(self, title: str, icon_id: Optional[str] = None, fallback: Optional[str] = None) -> "TelegramCard":
        """Set card header (renders in bold outside blockquote)."""
        self._title = title
        self._title_icon_id = icon_id
        self._title_fallback = fallback
        return self

    def add_line(self, text: str, icon_id: Optional[str] = None, fallback: Optional[str] = None) -> "TelegramCard":
        """Add an item/line to the body blockquote."""
        if icon_id:
            prefix = tg_emoji(icon_id, fallback) + " "
        else:
            prefix = ""
        self._lines.append(f"{prefix}{text}")
        return self

    def add_raw_line(self, raw_html: str) -> "TelegramCard":
        """Add raw HTML line to the body."""
        self._lines.append(raw_html)
        return self

    def with_spacer(self, enabled: bool = True) -> "TelegramCard":
        """Ensure full-width rendering across mobile and desktop clients."""
        self._use_spacer = enabled
        return self

    def set_signature(self, text: str, expandable: bool = True) -> "TelegramCard":
        """Set footer signature (e.g., bot brand or help text)."""
        self._signature = text
        self._signature_expandable = expandable
        return self

    def build(self) -> str:
        """Render the complete message in Telegram HTML parse mode."""
        parts = []

        # 1. Header (Outside blockquote)
        if self._title:
            if self._title_icon_id:
                title_icon = tg_emoji(self._title_icon_id, self._title_fallback) + " "
            else:
                title_icon = ""
            parts.append(f"<b>{title_icon}{self._title}</b>\n")

        # 2. Body (Inside blockquote)
        if self._lines:
            body_content = "\n\n".join(self._lines)
            if self._use_spacer:
                body_content += f"\n{FULL_WIDTH_SPACER}"
            parts.append(f"<blockquote><i>{body_content}</i></blockquote>")

        # 3. Signature (Expandable blockquote)
        if self._signature:
            exp_attr = " expandable" if self._signature_expandable else ""
            parts.append(f"\n<blockquote{exp_attr}><i>{self._signature}</i></blockquote>")

        return "\n".join(parts).strip()


def build_inline_button(
    text: str,
    callback_data: Optional[str] = None,
    url: Optional[str] = None,
    icon_custom_emoji_id: Optional[str] = None,
    style: Optional[str] = None,
):
    """
    Helper to construct an Aiogram 3 InlineKeyboardButton with custom emoji icon
    and optional button style (Bot API 7.0+ & 10.x).
    
    Rules enforced:
    - Never place unicode emojis in text when icon_custom_emoji_id is provided.
    - Avoid parentheses or price tags inside button text.
    """
    try:
        from aiogram.types import InlineKeyboardButton
    except ImportError:
        raise ImportError("aiogram is required to use build_inline_button. Run: pip install aiogram")

    kwargs = {"text": text}
    if callback_data:
        kwargs["callback_data"] = callback_data
    if url:
        kwargs["url"] = url
    if icon_custom_emoji_id:
        kwargs["icon_custom_emoji_id"] = str(icon_custom_emoji_id)
    if style:
        kwargs["style"] = style  # 'primary', 'success', 'danger'

    return InlineKeyboardButton(**kwargs)

"""
Tests for TelegramCard and helper utilities.
"""
import pytest
from telegram_premium_emojis import TelegramCard, tg_emoji, validation_badge, CommonIcons, FULL_WIDTH_SPACER


def test_tg_emoji():
    result = tg_emoji(CommonIcons.DIAMOND)
    assert result == f'<tg-emoji emoji-id="{CommonIcons.DIAMOND}">💎</tg-emoji>'

    custom_fb = tg_emoji(CommonIcons.DIAMOND, fallback="🔹")
    assert custom_fb == f'<tg-emoji emoji-id="{CommonIcons.DIAMOND}">🔹</tg-emoji>'


def test_validation_badge():
    badge = validation_badge("success", "Operation completed")
    assert "✅" in badge
    assert f'emoji-id="{CommonIcons.SUCCESS}"' in badge
    assert "Operation completed" in badge


def test_telegram_card_structure():
    card = (
        TelegramCard()
        .set_title("Test Title", icon_id=CommonIcons.CROWN)
        .add_line("Line 1 of content", icon_id=CommonIcons.CHECK if hasattr(CommonIcons, 'CHECK') else CommonIcons.SUCCESS)
        .add_line("Line 2 of content")
        .with_spacer(True)
        .set_signature("Made with OsonPDF", expandable=True)
        .build()
    )

    # 1. Title must be bold and outside blockquote
    assert f"<b><tg-emoji emoji-id=\"{CommonIcons.CROWN}\">👑</tg-emoji> Test Title</b>" in card
    # 2. Body must be inside <blockquote><i>...</i></blockquote>
    assert "<blockquote><i>" in card
    assert "Line 1 of content" in card
    assert FULL_WIDTH_SPACER in card
    assert "</i></blockquote>" in card
    # 3. Signature must be expandable blockquote
    assert "<blockquote expandable><i>Made with OsonPDF</i></blockquote>" in card

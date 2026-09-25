"""
Tests for validator.py linter rules.
"""
from pathlib import Path
from telegram_premium_emojis.validator import validate_file


def test_validator_detects_broken_tag(tmp_path):
    bad_file = tmp_path / "bad_syntax.py"
    bad_file.write_text('text = "<tg-emoji emoji-id=\'123\'>Broken tag without closing"', encoding="utf-8")

    issues = validate_file(bad_file)
    assert len(issues) >= 1
    assert any(i["code"] == "E001" for i in issues)


def test_validator_detects_button_emoji_redundancy(tmp_path):
    btn_file = tmp_path / "redundant_button.py"
    btn_file.write_text(
        'button = InlineKeyboardButton(text="💎 Topup Balance", icon_custom_emoji_id="5807465992363710697")',
        encoding="utf-8"
    )

    issues = validate_file(btn_file)
    assert any(i["code"] == "W002" for i in issues)


def test_validator_clean_code(tmp_path):
    clean_file = tmp_path / "clean_code.py"
    clean_file.write_text(
        'button = InlineKeyboardButton(text="Topup Balance", icon_custom_emoji_id="5807465992363710697")\n'
        'msg = "<tg-emoji emoji-id=\'5807465992363710697\'>💎</tg-emoji> Balance"',
        encoding="utf-8"
    )

    issues = validate_file(clean_file)
    assert len(issues) == 0

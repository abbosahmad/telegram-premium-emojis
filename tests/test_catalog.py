"""
Tests for catalog data integrity.
"""
import json
from pathlib import Path

CATALOG_DIR = Path(__file__).resolve().parent.parent / "catalog"


def test_all_emojis_json():
    all_emojis_path = CATALOG_DIR / "all_emojis.json"
    assert all_emojis_path.exists(), "all_emojis.json does not exist"

    data = json.loads(all_emojis_path.read_text(encoding="utf-8"))
    assert isinstance(data, list)
    assert len(data) > 800, f"Expected >800 emojis, got {len(data)}"

    # Check first item schema
    item = data[0]
    assert "id" in item
    assert "emoji" in item
    assert "pack" in item
    assert "html_tag" in item
    assert item["id"].isdigit()


def test_curated_packs_json():
    packs_path = CATALOG_DIR / "curated_packs.json"
    assert packs_path.exists(), "curated_packs.json does not exist"

    packs = json.loads(packs_path.read_text(encoding="utf-8"))
    assert isinstance(packs, dict)
    assert "TgAndroidIcons" in packs
    assert "NewsEmoji" in packs
    assert "RoboEmoji" in packs
    assert packs["TgAndroidIcons"]["count"] > 400

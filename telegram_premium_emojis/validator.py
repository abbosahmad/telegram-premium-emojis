"""
Telegram Premium Emojis Code Validator & Linter
Detects UI/UX anti-patterns, malformed custom emoji tags, and button text issues in Telegram Bot code.
"""
import os
import re
import sys
import argparse
from pathlib import Path
from typing import List, Dict, Any


UNICODE_EMOJI_PATTERN = re.compile(
    r"[\U00010000-\U0010ffff\u2600-\u26ff\u2700-\u27bf\u2300-\u23ff\u2b50-\u2b55\u200d\ufe0f]"
)
TG_EMOJI_PATTERN = re.compile(r"<tg-emoji\s+emoji-id=['\"]?(\d+)['\"]?>([^<]*)</tg-emoji>", re.IGNORECASE)
MALFORMED_TG_EMOJI = re.compile(r"<tg-emoji(?![^>]*</tg-emoji>)", re.IGNORECASE)
PAREN_LABEL_PATTERN = re.compile(r"\((?:Bepul|Free|Бесплатно|\d+\s*(?:MB|GB|so'm|сум|USD))\)", re.IGNORECASE)


def validate_file(file_path: Path) -> List[Dict[str, Any]]:
    """Validate a single Python or text file for Telegram UI / Emoji anti-patterns."""
    issues = []
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return [{"line": 0, "severity": "error", "message": f"Could not read file: {e}"}]

    lines = content.splitlines()

    for idx, line in enumerate(lines, start=1):
        # 1. Check for broken <tg-emoji> tags
        if "<tg-emoji" in line:
            # Check if closed on same line or within context
            if not re.search(r"</tg-emoji>", line) and not (idx < len(lines) and "</tg-emoji>" in lines[idx]):
                issues.append({
                    "line": idx,
                    "severity": "error",
                    "code": "E001",
                    "message": "Malformed or unclosed <tg-emoji> tag.",
                    "snippet": line.strip()
                })

            # Check if tag has an empty fallback
            for match in TG_EMOJI_PATTERN.finditer(line):
                eid, fallback = match.groups()
                if not fallback or fallback.strip() == "":
                    issues.append({
                        "line": idx,
                        "severity": "warning",
                        "code": "W001",
                        "message": f"Custom emoji ID {eid} has an empty fallback. Always provide a fallback unicode emoji.",
                        "snippet": match.group(0)
                    })

        # 2. Check for button definition with unicode emoji in text while using icon_custom_emoji_id
        if "InlineKeyboardButton" in line or "builder.button(" in line:
            has_custom_icon = "icon_custom_emoji_id" in line
            text_match = re.search(r'text\s*=\s*["\']([^"\']+)["\']', line)
            if text_match:
                btn_text = text_match.group(1)
                
                # Check for unicode emoji in button text when icon_custom_emoji_id is used
                if has_custom_icon and UNICODE_EMOJI_PATTERN.search(btn_text):
                    issues.append({
                        "line": idx,
                        "severity": "warning",
                        "code": "W002",
                        "message": f"Avoid putting unicode emojis in button text ('{btn_text}') when 'icon_custom_emoji_id' is already provided.",
                        "snippet": line.strip()
                    })

                # Check for parenthesized tags in button text
                if PAREN_LABEL_PATTERN.search(btn_text):
                    issues.append({
                        "line": idx,
                        "severity": "info",
                        "code": "I001",
                        "message": f"Avoid parenthesized promotional tags in button text ('{btn_text}'). Keep button labels clean and concise.",
                        "snippet": line.strip()
                    })

    return issues


def validate_path(target_path: Path) -> Dict[str, List[Dict[str, Any]]]:
    """Scan a file or directory recursively."""
    results = {}
    if target_path.is_file():
        files = [target_path]
    else:
        files = [
            p for p in target_path.rglob("*.py")
            if not any(part.startswith(".") or part in ("venv", ".venv", "__pycache__", "build", "dist") for part in p.parts)
        ]

    for f in files:
        issues = validate_file(f)
        if issues:
            results[str(f)] = issues

    return results


def main():
    parser = argparse.ArgumentParser(description="Lint Telegram bot code for Premium Emoji & UI standards.")
    parser.add_argument("target", nargs="?", default=".", help="File or folder to scan")
    parser.add_argument("--strict", action="store_true", help="Exit with non-zero code on warnings")

    args = parser.parse_args()
    target = Path(args.target).resolve()

    if not target.exists():
        print(f"❌ Path not found: {target}")
        sys.exit(1)

    print(f"🔍 Scanning for Telegram UI & Emoji issues in: {target} ...\n")
    results = validate_path(target)

    total_issues = sum(len(v) for v in results.values())
    errors = sum(1 for v in results.values() for i in v if i["severity"] == "error")
    warnings = sum(1 for v in results.values() for i in v if i["severity"] == "warning")

    if not results:
        print("✅ Great job! No Telegram Premium Emoji or UI anti-patterns found.")
        sys.exit(0)

    for file_path, issues in results.items():
        print(f"📄 {file_path}")
        for iss in issues:
            sev_icon = "❌" if iss["severity"] == "error" else ("⚠️" if iss["severity"] == "warning" else "ℹ️")
            code = iss.get("code", "")
            print(f"  Line {iss['line']}: {sev_icon} [{code}] {iss['message']}")
            if iss.get("snippet"):
                print(f"    --> {iss['snippet']}")
        print()

    print(f"Summary: {total_issues} issues ({errors} errors, {warnings} warnings).")

    if errors > 0 or (args.strict and warnings > 0):
        sys.exit(1)


if __name__ == "__main__":
    main()

"""
Telegram Custom Emoji Pack Scanner CLI & Library
Extracts custom emoji IDs from any public Telegram sticker/emoji pack using Bot API.
"""
import sys
import os
import json
import asyncio
import argparse
from typing import List, Dict, Any, Optional

try:
    import aiohttp
except ImportError:
    aiohttp = None


async def fetch_sticker_set(
    bot_token: str,
    pack_name: str,
    session: Optional["aiohttp.ClientSession"] = None
) -> Dict[str, Any]:
    """Fetch sticker set metadata directly from Telegram Bot API."""
    if not aiohttp:
        raise ImportError("aiohttp is required for scanner. Run: pip install aiohttp")

    close_session = False
    if session is None:
        session = aiohttp.ClientSession()
        close_session = True

    try:
        url = f"https://api.telegram.org/bot{bot_token}/getStickerSet"
        async with session.get(url, params={"name": pack_name}) as resp:
            data = await resp.json()
            return data
    finally:
        if close_session:
            await session.close()


async def scan_pack(
    pack_name: str,
    bot_token: Optional[str] = None,
    test_chat_id: Optional[int] = None,
    verify_live: bool = False
) -> Dict[str, Any]:
    """
    Scan a pack and extract all custom emoji IDs.
    
    If verify_live is True and test_chat_id is provided, sends a test message
    for each emoji and deletes it immediately to guarantee the bot has permission
    to use the custom emoji.
    """
    if not aiohttp:
        raise ImportError("aiohttp is required for scanner. Run: pip install aiohttp")

    token = bot_token or os.getenv("BOT_TOKEN")
    if not token:
        raise ValueError("BOT_TOKEN must be provided as an argument or environment variable.")

    async with aiohttp.ClientSession() as session:
        data = await fetch_sticker_set(token, pack_name, session)

        if not data.get("ok"):
            err = data.get("description", "Unknown error")
            return {"ok": False, "error": f"Failed to fetch pack '{pack_name}': {err}"}

        result = data["result"]
        stickers = result.get("stickers", [])
        title = result.get("title", pack_name)
        is_custom_emoji = result.get("is_custom_emoji", result.get("is_animated", True))

        extracted_emojis = []
        working = []
        broken = []

        base_url = f"https://api.telegram.org/bot{token}"

        for idx, sticker in enumerate(stickers):
            eid = sticker.get("custom_emoji_id")
            emoji_char = sticker.get("emoji", "✨")

            if not eid:
                continue

            entry = {
                "id": str(eid),
                "emoji": emoji_char,
                "html": f'<tg-emoji emoji-id="{eid}">{emoji_char}</tg-emoji>'
            }
            extracted_emojis.append(entry)

            # Optional live test
            if verify_live and test_chat_id:
                test_text = f"<tg-emoji emoji-id='{eid}'>{emoji_char}</tg-emoji>"
                try:
                    async with session.post(
                        f"{base_url}/sendMessage",
                        json={"chat_id": test_chat_id, "text": test_text, "parse_mode": "HTML"}
                    ) as resp:
                        res = await resp.json()
                        if res.get("ok"):
                            msg_id = res["result"]["message_id"]
                            # Clean up immediately
                            await session.post(
                                f"{base_url}/deleteMessage",
                                json={"chat_id": test_chat_id, "message_id": msg_id}
                            )
                            working.append(entry)
                        else:
                            broken.append(entry)
                except Exception:
                    broken.append(entry)
                await asyncio.sleep(0.1)

        return {
            "ok": True,
            "pack_name": pack_name,
            "title": title,
            "count": len(extracted_emojis),
            "emojis": working if (verify_live and test_chat_id) else extracted_emojis,
            "broken_count": len(broken) if (verify_live and test_chat_id) else 0
        }


def main():
    parser = argparse.ArgumentParser(
        description="Scan any Telegram custom emoji pack and extract emoji IDs."
    )
    parser.add_argument("packs", nargs="+", help="Names of the sticker packs (e.g. TgAndroidIcons TajalyanEmoji)")
    parser.add_argument("--token", "-t", default=os.getenv("BOT_TOKEN"), help="Telegram Bot Token")
    parser.add_argument("--format", "-f", choices=["json", "table", "python"], default="table", help="Output format")
    parser.add_argument("--test-chat", type=int, default=os.getenv("ADMIN_ID"), help="Optional Chat ID to test live delivery")
    parser.add_argument("--verify", action="store_true", help="Send and delete test message to verify bot permission")
    parser.add_argument("--out", "-o", help="Optional output file path")

    args = parser.parse_args()

    if not args.token:
        print("❌ Error: Telegram Bot Token is required! Pass --token or set BOT_TOKEN environment variable.")
        sys.exit(1)

    async def run():
        results = []
        for pack in args.packs:
            print(f"🔍 Scanning pack: {pack} ...", file=sys.stderr)
            res = await scan_pack(pack, bot_token=args.token, test_chat_id=args.test_chat, verify_live=args.verify)
            if res.get("ok"):
                print(f"✅ Found {res['count']} emojis in '{res['title']}'", file=sys.stderr)
                results.append(res)
            else:
                print(f"❌ {res.get('error')}", file=sys.stderr)

        if args.format == "json":
            output = json.dumps(results, indent=2, ensure_ascii=False)
        elif args.format == "python":
            py_dict = {}
            for r in results:
                py_dict[r["pack_name"]] = {item["emoji"]: item["id"] for item in r["emojis"]}
            output = f"# Auto-generated Telegram Custom Emoji IDs\nEMOJI_PACKS = {repr(py_dict)}"
        else:
            lines = []
            for r in results:
                lines.append(f"\n### Pack: {r['title']} ({r['pack_name']}) — {r['count']} emojis\n")
                lines.append("| # | Emoji | Custom Emoji ID | HTML Tag |")
                lines.append("|---|---|---|---|")
                for i, item in enumerate(r["emojis"], 1):
                    lines.append(f"| {i} | {item['emoji']} | `{item['id']}` | `{item['html']}` |")
            output = "\n".join(lines)

        if args.out:
            with open(args.out, "w", encoding="utf-8") as f:
                f.write(output)
            print(f"\n📁 Saved output to {args.out}", file=sys.stderr)
        else:
            print(output)

    asyncio.run(run())


if __name__ == "__main__":
    main()

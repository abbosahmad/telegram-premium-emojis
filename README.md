# Telegram Premium Emojis & UI Toolkit 💎

<p align="center">
  <a href="https://pypi.org/project/telegram-premium-emojis/"><img src="https://img.shields.io/pypi/v/telegram-premium-emojis?color=blue&style=for-the-badge&logo=pypi&logoColor=white" alt="PyPI Version"></a>
  <img src="https://img.shields.io/badge/Telegram_Bot_API-7.0%20%7C%208.0%2B-blue?logo=telegram&style=for-the-badge" alt="Telegram Bot API">
  <img src="https://img.shields.io/badge/Aiogram-3.x_Ready-2ea44f?style=for-the-badge" alt="Aiogram 3">
  <img src="https://img.shields.io/badge/Catalog-1%2C920%2B_Custom_Emojis-orange?style=for-the-badge" alt="Catalog">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License">
</p>

<p align="center">
  <b>The complete open-source toolkit and AI Agent Skill for Telegram Bot Premium Custom Emojis, Aiogram 3 modern card layouts, inline keyboard custom emoji icons, and automated pack discovery.</b>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#card-ui-architecture">Card UI Architecture</a> •
  <a href="#catalog--emoji-ids">Catalog & Emoji IDs</a> •
  <a href="#cli-tools">CLI Tools</a> •
  <a href="#ai-agent-skill">AI Agent Skill</a> •
  <a href="README.uz.md">O'zbekcha Qo'llanma</a>
</p>

---

## 🚀 Why This Project?

Since Telegram introduced **Bot API 7.0+ & 8.0+**, bots can display animated custom emojis inside messages (`<tg-emoji>`) and natively attach custom emoji icons to inline keyboard buttons (`icon_custom_emoji_id`).

However, most developers and AI coding agents still struggle with:
1. **Finding valid custom emoji IDs** from public packs without tedious manual inspection.
2. **Ugly button styling:** Accidental emoji duplication like `text="💎 Balance"` alongside `icon_custom_emoji_id`.
3. **Broken cards:** Messages collapsing into narrow, squished blockquotes because of missing full-width spacing.
4. **Missing fallbacks:** Breaking on older Telegram clients because of empty or missing fallback unicode emojis.

**`telegram-premium-emojis` solves all of these once and for all.**

---

## ✨ Key Features

- **💎 920+ Curated Emoji Database:** Verified custom emoji IDs across 6 top packs (`TgAndroidIcons`, `tgmacicons`, `vector_icons_by_fStikBot`, `NewsEmoji`, `RoboEmoji`, `StatusEmoji`).
- **🎴 Fluent `TelegramCard` Builder:** Generate gorgeous, full-width Telegram cards with bold titles, quote bodies, invisible spacers, and expandable signatures in 3 lines of code.
- **🔘 Smart Button Helper:** Aiogram 3 `build_inline_button` with clean text enforcement and modern color styling (`primary`, `success`, `danger`).
- **🔍 Pack Scanner CLI:** Scan *any* public Telegram sticker/emoji set via Telegram Bot API and extract all working custom emoji IDs in seconds.
- **🛡️ Code Linter / Validator:** Scan your bot repository for broken `<tg-emoji>` tags, unicode button duplication, or promotional brackets.
- **🤖 Universal AI Agent Skill:** Out-of-the-box `SKILL.md` compatible with Antigravity, Claude Code, Cursor, and Copilot.

---

## 📦 Installation

```bash
pip install telegram-premium-emojis
```

Or clone directly for development:
```bash
git clone https://github.com/abbosahmad/telegram-premium-emojis.git
cd telegram-premium-emojis
pip install -e ".[dev]"
```

---

## ⚡ Quick Start

### 1. Generate a Modern Card UI with Aiogram 3

```python
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import InlineKeyboardBuilder

from telegram_premium_emojis import TelegramCard, CommonIcons, build_inline_button

bot = Bot(token="YOUR_BOT_TOKEN", default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

@dp.message()
async def start_handler(message: types.Message):
    # 1. Build a responsive Telegram Card
    card = (
        TelegramCard()
        .set_title("PDF Converter Suite", icon_id=CommonIcons.DOCUMENT)
        .add_line("Convert PDF documents to editable Word & Excel.", icon_id=CommonIcons.SPARKLES)
        .add_line("Max file size: 100 MB", icon_id=CommonIcons.ATTACH)
        .add_line("Status: All conversion servers operational", icon_id=CommonIcons.SUCCESS)
        .with_spacer()  # Stretches card to full width
        .set_signature("@mybot • Fast, Secure & Free", expandable=True)
        .build()
    )

    # 2. Build keyboard with custom emoji icons
    builder = InlineKeyboardBuilder()
    builder.row(
        build_inline_button(
            text="Upload Document",
            callback_data="upload",
            icon_custom_emoji_id=CommonIcons.UPLOAD,
            style="success"  # Highlights button in green
        )
    )
    builder.row(
        build_inline_button(
            text="Settings",
            callback_data="settings",
            icon_custom_emoji_id=CommonIcons.SETTINGS
        ),
        build_inline_button(
            text="Back",
            callback_data="back",
            icon_custom_emoji_id=CommonIcons.BACK,
            style="danger"  # Back/Cancel in red
        )
    )

    await message.answer(card, reply_markup=builder.as_markup())
```

---

## 📐 Card UI Architecture

Every card generated adheres to the proven **Telegram Card Architecture**:

```
<b><tg-emoji emoji-id="...">👑</tg-emoji> Title (Outside Blockquote)</b>

<blockquote><i><tg-emoji emoji-id="...">✨</tg-emoji> First parameter or description

<tg-emoji emoji-id="...">⚡️</tg-emoji> Second parameter or note
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</i></blockquote>

<blockquote expandable><i>Verified by @BotName</i></blockquote>
```

### Why does this look so much better?
1. **Title Outside Quote:** Prevents header text from blending into the quote italic styling.
2. **Full-Width Invisible Spacer:** Telegram's layout engine collapses quotes without it. The invisible Braille spacer (`FULL_WIDTH_SPACER`) guarantees crisp full-width presentation on iOS, Android, and Desktop.
3. **Expandable Signature:** Uses `<blockquote expandable>` for clean brand attribution without cluttering primary content.

---

## 📚 Catalog & Top 25 Essential IDs

Browse the complete 920+ database in [`catalog/catalog.md`](catalog/catalog.md) or [`catalog/all_emojis.json`](catalog/all_emojis.json).

| Purpose | Fallback | Custom Emoji ID | HTML Syntax |
|---|---|---|---|
| **Back / Previous** | ⬅️ | `5877536313623711363` | `<tg-emoji emoji-id="5877536313623711363">⬅️</tg-emoji>` |
| **Home / Menu** | 🏠 | `5807868868886009920` | `<tg-emoji emoji-id="5807868868886009920">🏠</tg-emoji>` |
| **Confirm / Success**| ✅ | `5920052658743283381` | `<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji>` |
| **Cancel / Close** | ❌ | `5258226313285607065` | `<tg-emoji emoji-id="5258226313285607065">❌</tg-emoji>` |
| **Diamond / Tokens** | 💎 | `5807465992363710697` | `<tg-emoji emoji-id="5807465992363710697">💎</tg-emoji>` |
| **Star / Premium** | ⭐️ | `5874948844935974490` | `<tg-emoji emoji-id="5874948844935974490">⭐️</tg-emoji>` |
| **Lightning / Speed**| ⚡️ | `5843553939672274145` | `<tg-emoji emoji-id="5843553939672274145">⚡️</tg-emoji>` |
| **Crown / VIP** | 👑 | `5807868868886009920` | `<tg-emoji emoji-id="5807868868886009920">👑</tg-emoji>` |
| **Document** | 📄 | `5258477770735885832` | `<tg-emoji emoji-id="5258477770735885832">📄</tg-emoji>` |
| **Folder** | 📁 | `5875206779196935950` | `<tg-emoji emoji-id="5875206779196935950">📁</tg-emoji>` |
| **Download** | ⬇️ | `5258336354642697821` | `<tg-emoji emoji-id="5258336354642697821">⬇️</tg-emoji>` |
| **Upload** | ⬆️ | `5260652420052032852` | `<tg-emoji emoji-id="5260652420052032852">⬆️</tg-emoji>` |
| **Warning** | ⚠️ | `5258474669769497337` | `<tg-emoji emoji-id="5258474669769497337">⚠️</tg-emoji>` |
| **Information** | ℹ️ | `5258503720928288433` | `<tg-emoji emoji-id="5258503720928288433">ℹ️</tg-emoji>` |
| **Settings** | ⚙️ | `5258420634785947640` | `<tg-emoji emoji-id="5258420634785947640">⚙️</tg-emoji>` |

---

## 🛠️ CLI Tools

### 1. Scan Any Sticker / Emoji Pack
Extract custom emoji IDs directly from Telegram API:
```bash
python -m telegram_premium_emojis.scanner TgAndroidIcons TajalyanEmoji --token YOUR_BOT_TOKEN
```
Export directly to JSON:
```bash
python -m telegram_premium_emojis.scanner TgAndroidIcons --token YOUR_BOT_TOKEN --format json --out icons.json
```

### 2. Lint & Validate Your Bot Codebase
Scan your bot code for UI anti-patterns and emoji errors:
```bash
python -m telegram_premium_emojis.validator path/to/your/bot/
```
Catches:
- Malformed `<tg-emoji>` tags.
- Missing fallback emojis.
- Redundant unicode emoji in button text when `icon_custom_emoji_id` is supplied.
- Marketing parentheses in button labels like `(Free)` or `(Bepul)`.

---

## 🤖 AI Agent Skill (`SKILL.md`)

This repository includes a standalone [`SKILL.md`](SKILL.md) file designed for AI coding agents:
- **Google Antigravity:** Place inside `.agents/skills/telegram-premium-emojis/SKILL.md`.
- **Claude Code:** Load into project instructions.
- **Cursor / Copilot:** Reference in `.cursorrules` or context.

When active, your AI assistant will write Telegram bot code using proper premium custom emoji tags, correct fallback emojis, clean button text, and blockquote card layouts automatically!

---

## 🤝 Contributing

Contributions are warmly welcome! Discover a new high-quality custom emoji pack? Submit a PR adding it to `catalog/curated_packs.json`. Read [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📄 License

MIT License © 2026 Abbos & OsonPDF Open Source Community.

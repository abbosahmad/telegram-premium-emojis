---
name: telegram-premium-emojis
description: "Comprehensive guide, design system, and code generator for Telegram Bot Premium Custom Emojis, Aiogram 3 card UI, icon_custom_emoji_id inline buttons, and sticker pack discovery."
---

# Telegram Premium Emojis & UI Design System (SKILL.md)

Use this skill whenever you are designing, modifying, or auditing Telegram bots using Aiogram 3, python-telegram-bot, or any Telegram Bot API 7.0+ framework. This skill teaches the agent how to properly apply **Telegram Custom Emojis**, inline button icons (`icon_custom_emoji_id`), button styles (`primary`, `success`, `danger`), and modern card layouts.

---

## 1. Core Mechanics & HTML Syntax

### 1.1. In-Text Custom Emojis (`<tg-emoji>`)
In Telegram HTML parse mode, custom emojis are rendered using the `<tg-emoji>` tag:
```html
<tg-emoji emoji-id="5807465992363710697">💎</tg-emoji>
```

> [!CRITICAL]
> 1. **Fallback Emoji is Mandatory:** Always put a matching standard unicode emoji inside the tag (e.g., `💎` for diamond, `✅` for success). If the user's client is outdated or on a platform that does not support custom emojis, the fallback is shown. Empty tags like `<tg-emoji emoji-id="..."></tg-emoji>` are invalid.
> 2. **Double Quotes in HTML:** Always wrap `emoji-id` in double quotes: `emoji-id="5807465992363710697"`.

### 1.2. Inline Keyboard Custom Emoji Icons (`icon_custom_emoji_id`)
Telegram Bot API 7.0+ supports custom emojis natively attached to inline buttons:
```python
from aiogram.types import InlineKeyboardButton

button = InlineKeyboardButton(
    text="Starter Pack",
    callback_data="buy_starter",
    icon_custom_emoji_id="5807465992363710697",
    style="primary"  # Optional: 'primary' (blue), 'success' (green), 'danger' (red)
)
```

---

## 2. The 5 Golden Rules of Telegram Bot UI

### Rule 1: No Duplicate Unicode Emojis in Button Text
❌ **WRONG:**
```python
InlineKeyboardButton(text="💎 Starter Pack", icon_custom_emoji_id="5807465992363710697")
```
*(This renders two diamond icons next to each other on the user's screen)*

✅ **CORRECT:**
```python
InlineKeyboardButton(text="Starter Pack", icon_custom_emoji_id="5807465992363710697")
```

### Rule 2: Clean Button Labels
Never clutter button text with parenthesized qualifiers, prices, or marketing words:
- ❌ `Birlashtirish (Bepul)` ➔ ✅ `Birlashtirish`
- ❌ `Antiplagiat (DOCX)` ➔ ✅ `Antiplagiat`
- ❌ `To'lov (19 000 so'm)` ➔ ✅ `Starter: 19 000 so'm`

### Rule 3: The Card Layout Architecture
All informational cards, greetings, task status messages, and results must follow the **Card Layout Architecture**:
```
<b><tg-emoji emoji-id="...">👑</tg-emoji> Card Title Here</b>

<blockquote><i><tg-emoji emoji-id="...">✨</tg-emoji> Feature or description line 1

<tg-emoji emoji-id="...">📄</tg-emoji> Feature or description line 2

<tg-emoji emoji-id="...">⚡️</tg-emoji> Feature or description line 3
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</i></blockquote>

<blockquote expandable><i>✅ Prepared by @YourBot</i></blockquote>
```

1. **Title:** Bold (`<b>...</b>`), placed on a plain line **OUTSIDE** the blockquote.
2. **Body:** Inside `<blockquote><i>...</i></blockquote>` with double newlines between items.
3. **Full-Width Invisible Spacer:** Always include `⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀` (`FULL_WIDTH_SPACER`) at the end of the blockquote to force Telegram mobile and desktop clients to stretch the card to full width.
4. **Signature:** Placed in `<blockquote expandable><i>...</i></blockquote>` at the very bottom.

### Rule 4: Visual Icon Families (Separation of Concerns)
Never mix visual roles. Use distinct custom emoji families:
- **Navigation:**
  - `Back`: Always use back arrow (`5877536313623711363`).
  - `Home / Main Menu`: Always use home icon (`5807868868886009920`). Never use back for home.
- **Validation / Status (in-text alerts):**
  - `Success`: `5920052658743283381` (✅)
  - `Error`: `5258226313285607065` (❌)
  - `Warning`: `5258474669769497337` (⚠️)
  - `Info`: `5258503720928288433` (ℹ️)
  - `Pending`: `5258419835922030550` (⏳)

### Rule 5: Button Styles
Telegram Bot API 10.x and Aiogram 3 support button color styles:
- `primary`: Default neutral/blue button for normal actions.
- `success`: Green button, used for the primary positive action or recommended purchase tier.
- `danger`: Red button, strictly reserved for `Back`, `Cancel`, or destructive actions (`Delete`).

### Rule 6: In-Text Data, Statistics & Gamification Cards
Never send raw, unstyled Unicode emojis in user profiles, dashboards, statistics, or gamification messages. Always render all data points as verified `<tg-emoji>` tags inside a card layout.

❌ **WRONG (Raw Unicode Emojis — looks unpolished & dated):**
```html
📊 Shaxsiy Statistika

👤 Abbos (@AbbosA)
🆔 ID: 5654706656

🏆 Umumiy ball (XP): 71 ball
📈 Umumiy reytingdagi o'rni: #7
🎯 Yechilgan testlar: 11 ta
📁 Yaratilgan testlar: 4 ta
🔥 Kunlik seriya: 1 kun
⚡ Kreditlar balansi: 3288 ta (Standart)

Har bir to'g'ri javob uchun + 1 XP olasiz va umumiy reytingda ko'tarilasiz! 🚀
```

✅ **CORRECT (Full Telegram Premium Card UI with `<tg-emoji>` & spacer):**
```html
<b><tg-emoji emoji-id="5877485980901971030">📊</tg-emoji> Shaxsiy Statistika</b>

<tg-emoji emoji-id="5771887475421090729">👤</tg-emoji> <b>Abbos</b> (@AbbosA)
<tg-emoji emoji-id="5258477770735885832">🆔</tg-emoji> ID: <code>5654706656</code>

<blockquote><tg-emoji emoji-id="5961051261204696786">🏆</tg-emoji> <b>Umumiy ball (XP):</b> 71 ball
<tg-emoji emoji-id="5776219138917668486">📈</tg-emoji> <b>Umumiy reytingdagi o'rni:</b> #7
<tg-emoji emoji-id="5920052658743283381">🎯</tg-emoji> <b>Yechilgan testlar:</b> 11 ta
<tg-emoji emoji-id="5875206779196935950">📁</tg-emoji> <b>Yaratilgan testlar:</b> 4 ta
<tg-emoji emoji-id="6008118472066732010">🔥</tg-emoji> <b>Kunlik seriya:</b> 1 kun
<tg-emoji emoji-id="5843553939672274145">⚡</tg-emoji> <b>Kreditlar balansi:</b> 3288 ta (Standart)
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀</blockquote>

<i>Har bir to'g'ri javob uchun +1 XP olasiz va umumiy reytingda ko'tarilasiz! <tg-emoji emoji-id="5875506366050734240">🚀</tg-emoji></i>
```

---

## 3. Essential Custom Emoji IDs Quick-Reference

| Role | Fallback | Custom Emoji ID | Full HTML Tag |
|---|---|---|---|
| **Back** | ⬅️ | `5877536313623711363` | `<tg-emoji emoji-id="5877536313623711363">⬅️</tg-emoji>` |
| **Home** | 🏠 | `5807868868886009920` | `<tg-emoji emoji-id="5807868868886009920">🏠</tg-emoji>` |
| **Confirm / Done** | ✅ | `5920052658743283381` | `<tg-emoji emoji-id="5920052658743283381">✅</tg-emoji>` |
| **Cancel** | ❌ | `5258226313285607065` | `<tg-emoji emoji-id="5258226313285607065">❌</tg-emoji>` |
| **Diamond / VIP** | 💎 | `5807465992363710697` | `<tg-emoji emoji-id="5807465992363710697">💎</tg-emoji>` |
| **Star / Premium** | ⭐️ | `5874948844935974490` | `<tg-emoji emoji-id="5874948844935974490">⭐️</tg-emoji>` |
| **Lightning / Energy** | ⚡️ | `5843553939672274145` | `<tg-emoji emoji-id="5843553939672274145">⚡️</tg-emoji>` |
| **Crown / Leader** | 👑 | `5807868868886009920` | `<tg-emoji emoji-id="5807868868886009920">👑</tg-emoji>` |
| **Stats / Analytics** | 📊 | `5877485980901971030` | `<tg-emoji emoji-id="5877485980901971030">📊</tg-emoji>` |
| **Growth / Rank** | 📈 | `5776219138917668486` | `<tg-emoji emoji-id="5776219138917668486">📈</tg-emoji>` |
| **Trophy / XP** | 🏆 | `5961051261204696786` | `<tg-emoji emoji-id="5961051261204696786">🏆</tg-emoji>` |
| **Target / Goal** | 🎯 | `5920052658743283381` | `<tg-emoji emoji-id="5920052658743283381">🎯</tg-emoji>` |
| **Fire / Streak** | 🔥 | `6008118472066732010` | `<tg-emoji emoji-id="6008118472066732010">🔥</tg-emoji>` |
| **Rocket / Boost** | 🚀 | `5875506366050734240` | `<tg-emoji emoji-id="5875506366050734240">🚀</tg-emoji>` |
| **User / Profile** | 👤 | `5771887475421090729` | `<tg-emoji emoji-id="5771887475421090729">👤</tg-emoji>` |
| **ID / Badge** | 🆔 | `5258477770735885832` | `<tg-emoji emoji-id="5258477770735885832">🆔</tg-emoji>` |
| **Medal Gold (1st)** | 🥇 | `5961051261204696786` | `<tg-emoji emoji-id="5961051261204696786">🥇</tg-emoji>` |
| **Medal Silver (2nd)**| 🥈 | `5447203607294265305` | `<tg-emoji emoji-id="5447203607294265305">🥈</tg-emoji>` |
| **Medal Bronze (3rd)**| 🥉 | `5453902265922376865` | `<tg-emoji emoji-id="5453902265922376865">🥉</tg-emoji>` |
| **Refresh** | 🔄 | `5260687119092817530` | `<tg-emoji emoji-id="5260687119092817530">🔄</tg-emoji>` |
| **Trash** | 🗑 | `5258130763148172425` | `<tg-emoji emoji-id="5258130763148172425">🗑</tg-emoji>` |
| **Document** | 📄 | `5258477770735885832` | `<tg-emoji emoji-id="5258477770735885832">📄</tg-emoji>` |
| **Folder** | 📁 | `5875206779196935950` | `<tg-emoji emoji-id="5875206779196935950">📁</tg-emoji>` |
| **Download** | ⬇️ | `5258336354642697821` | `<tg-emoji emoji-id="5258336354642697821">⬇️</tg-emoji>` |
| **Upload** | ⬆️ | `5260652420052032852` | `<tg-emoji emoji-id="5260652420052032852">⬆️</tg-emoji>` |
| **Card** | 💳 | `5258260149037965799` | `<tg-emoji emoji-id="5258260149037965799">💳</tg-emoji>` |
| **Coin** | 🪙 | `5258368777350816286` | `<tg-emoji emoji-id="5258368777350816286">🪙</tg-emoji>` |
| **Warning** | ⚠️ | `5258474669769497337` | `<tg-emoji emoji-id="5258474669769497337">⚠️</tg-emoji>` |
| **Info** | ℹ️ | `5258503720928288433` | `<tg-emoji emoji-id="5258503720928288433">ℹ️</tg-emoji>` |
| **Settings** | ⚙️ | `5258420634785947640` | `<tg-emoji emoji-id="5258420634785947640">⚙️</tg-emoji>` |
| **Search** | 🔍 | `5260341314095947411` | `<tg-emoji emoji-id="5260341314095947411">🔍</tg-emoji>` |
| **Edit** | ✏️ | `5839380464116175529` | `<tg-emoji emoji-id="5839380464116175529">✏️</tg-emoji>` |
| **Attach** | 📎 | `5260730055880876557` | `<tg-emoji emoji-id="5260730055880876557">📎</tg-emoji>` |
| **Sparkles**| ✨ | `5877318502947229960` | `<tg-emoji emoji-id="5877318502947229960">✨</tg-emoji>` |
| **Robot** | 🤖 | `5258093637450866522` | `<tg-emoji emoji-id="5258093637450866522">🤖</tg-emoji>` |


---

## 4. Production Code Recipes

### Recipe A: Using the `telegram-premium-emojis` Python Package
```python
from telegram_premium_emojis import TelegramCard, CommonIcons, build_inline_button
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Build Card
card_html = (
    TelegramCard()
    .set_title("PDF Siqish Xizmati", icon_id=CommonIcons.DOCUMENT)
    .add_line("Fayl hajmini sifatini yo'qotmasdan 80% gacha kamaytiradi.", icon_id=CommonIcons.SPARKLES)
    .add_line("Maksimal hajm: 200 MB", icon_id=CommonIcons.ATTACH)
    .with_spacer()
    .set_signature("OsonPDF • Tez va Xavfsiz", expandable=True)
    .build()
)

# Build Inline Keyboard
builder = InlineKeyboardBuilder()
builder.row(
    build_inline_button("Fayl yuborish", callback_data="upload", icon_custom_emoji_id=CommonIcons.UPLOAD, style="success")
)
builder.row(
    build_inline_button("Orqaga", callback_data="back", icon_custom_emoji_id=CommonIcons.BACK, style="danger")
)
```

### Recipe B: Manual Aiogram 3 Implementation (Zero-Dependency)
```python
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

SPACER = "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"

text = (
    '<b><tg-emoji emoji-id="5807465992363710697">💎</tg-emoji> Hisob Balansi</b>\n\n'
    '<blockquote><i><tg-emoji emoji-id="5874948844935974490">⭐️</tg-emoji> <b>Tarif:</b> Pro Max\n\n'
    '<tg-emoji emoji-id="5807465992363710697">💎</tg-emoji> <b>Tokenlar:</b> 120 ta\n\n'
    f'<tg-emoji emoji-id="5843553939672274145">⚡️</tg-emoji> <b>Limit:</b> Cheksiz\n{SPACER}</i></blockquote>\n\n'
    '<blockquote expandable><i>To\'lovlar Click va Payme orqali himoyalangan</i></blockquote>'
)

markup = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Token sotib olish", callback_data="topup", icon_custom_emoji_id="5807465992363710697", style="success")],
    [InlineKeyboardButton(text="Orqaga", callback_data="back", icon_custom_emoji_id="5877536313623711363", style="danger")]
])
```

---

## 5. Discovering & Scanning New Sticker Packs

To extract custom emoji IDs from any public pack (e.g. `TgAndroidIcons`, `TajalyanEmoji`):
```bash
python -m telegram_premium_emojis.scanner PackName --token <BOT_TOKEN> --format table
```
Or export directly to JSON:
```bash
python -m telegram_premium_emojis.scanner PackName --token <BOT_TOKEN> --format json --out custom_pack.json
```

---

## 6. Code Auditing & Linting

Run the built-in validator against any bot codebase:
```bash
python -m telegram_premium_emojis.validator path/to/bot/
```
It immediately catches:
- Unicode emojis placed inside button text with `icon_custom_emoji_id`.
- Unclosed or malformed `<tg-emoji>` tags.
- Promotional brackets `(Bepul)` in button labels.

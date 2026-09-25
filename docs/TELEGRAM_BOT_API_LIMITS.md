# Telegram Bot API: Custom Emoji Prerequisites & Technical Specifications

This document outlines the exact technical requirements, Bot API capabilities, and client compatibility rules for using Telegram Custom Emojis in bots.

---

## 1. Telegram Bot API Timeline & Support

| Bot API Version | Released | Key Custom Emoji Features |
|---|---|---|
| **Bot API 7.0** | December 2023 | Initial introduction of `<tg-emoji>` tag support in HTML & MarkdownV2 parse modes. |
| **Bot API 7.2** | March 2024 | Telegram Business integration; bots connected to business accounts gain full custom emoji rights. |
| **Bot API 7.10 / 8.0** | Late 2024 | Introduction of `icon_custom_emoji_id` in `InlineKeyboardButton`. |
| **Bot API 10.x** | 2025–2026 | Inline keyboard button color styles (`primary`, `success`, `danger`) and `disabled` attribute. |

---

## 2. Who Can Use Custom Emojis in Bots?

### Bot Permission Rules
Telegram applies specific permission policies regarding which bots can render custom emojis:

1. **Free / Standard Bots:**
   - Can send custom emojis from **default/official Telegram packs** (e.g., Telegram status icons, standard reactions).
   - If a bot attempts to send an emoji from an unauthorized third-party private pack, the Telegram Bot API may strip the custom emoji and display only the fallback unicode character.

2. **Telegram Business / Verified / Fragment Bots:**
   - Bots connected to Telegram Business or possessing a collectible username acquired via Fragment.com have elevated privileges to render custom emojis from any public sticker/emoji pack.

3. **User Client Rendering:**
   - **Telegram Premium Users:** Custom emojis are fully animated or rendered in high-definition vector graphics.
   - **Non-Premium Users:** Custom emojis are rendered as static icons in most official clients, or fallback to standard unicode emojis if not supported by the platform.

---

## 3. HTML Tag Specification

The tag format must strictly adhere to:
```html
<tg-emoji emoji-id="5807465992363710697">💎</tg-emoji>
```

### Technical Constraints:
1. **Double Quotes:** Use `emoji-id="..."` (or single quotes `emoji-id='...'`).
2. **Emoji ID Data Type:** Must be a valid 64-bit integer formatted as a string (typically 18 to 20 digits).
3. **Inner Text (Fallback):** Must contain exactly one unicode emoji representation. Empty inner content is treated as invalid and may cause `BadRequest: can't parse entities in message text`.
4. **MarkdownV2 Format:**
   ```markdown
   ![💎](tg://emoji?id=5807465992363710697)
   ```
   *(HTML mode `<tg-emoji>` is strongly recommended over MarkdownV2 due to Markdown's aggressive escaping requirements)*.

---

## 4. InlineKeyboardButton Specification

```json
{
  "text": "Start Task",
  "callback_data": "task_start",
  "icon_custom_emoji_id": "5920052658743283381",
  "style": "success"
}
```

- `icon_custom_emoji_id`: String containing the custom emoji ID.
- `style`: Optional string: `"primary"` (default blue/neutral), `"success"` (green), `"danger"` (red).
- When `icon_custom_emoji_id` is supplied, the Telegram client automatically prefixes the button text with the custom emoji icon.

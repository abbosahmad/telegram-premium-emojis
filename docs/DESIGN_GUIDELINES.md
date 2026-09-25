# Telegram Bot UI/UX Design System & Best Practices

Design in Telegram is not merely visual styling; it directly impacts user retention, trust, conversion rates, and task completion. This guide explains the core design system implemented in `telegram-premium-emojis`.

---

## 1. Visual Hierarchy: The Card Structure

Traditional bot messages look like raw walls of text. Modern bots structure messages into visual **Cards**:

```
[Title Zone]      --> Bold, outside blockquote. Grabs attention immediately.
[Body Blockquote] --> Italic, grouped parameters and descriptions.
[Full Spacer]     --> Invisible Braille spacer to standardize width.
[Action Keyboard] --> Clean buttons with dedicated emoji icons & color styling.
[Signature Zone]  --> Expandable quote for branding and secondary help.
```

### Why Title Outside the Blockquote?
When a title is placed inside a blockquote, it inherits the blockquote border and italic styling, blending into the body text. Placing the title above the blockquote creates visual separation, making it clear where the message header ends and where the content begins.

### Why the Full-Width Invisible Spacer?
Telegram clients dynamically adjust blockquote width based on the longest line in the quote. If a message contains short lines (e.g., "Status: Done"), the blockquote collapses into a narrow, squished box that looks broken on wide screens.

Adding the Braille whitespace character (`FULL_WIDTH_SPACER` = `⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀`) forces Telegram's layout engine to render the card at standard full bubble width.

---

## 2. Iconography & Visual Families

### Visual Roles Must Never Collide:
1. **Navigation Icons:**
   - Always use a dedicated Back arrow (`5877536313623711363`) for `Back / Orqaga / Назад`.
   - Always use a dedicated Home icon (`5807868868886009920`) for `Main Menu / Asosiy Menyu`.
   - Never use Back and Home interchangeably.

2. **Validation & Alerts:**
   - Reserve `✅`, `❌`, `⚠️`, `ℹ️`, `⏳` strictly for validation, notifications, and task statuses.
   - Do not use status icons for ordinary navigation buttons.

3. **Financial & Value:**
   - Use `💎` (Diamond) or `🪙` (Coin) for balance and credit tokens.
   - Use `👑` (Crown) or `⭐️` (Star) for subscriptions and premium tiers.

---

## 3. Button Hygiene

### Golden Rules:
1. **Never double-dip emojis:**
   If `icon_custom_emoji_id` is passed, do NOT include emojis in `text`.
   - ❌ `text="💎 Balance"` + `icon_custom_emoji_id="5807465992363710697"`
   - ✅ `text="Balance"` + `icon_custom_emoji_id="5807465992363710697"`

2. **No parenthesized promotional tags:**
   - ❌ `text="Generate Essay (Free)"`
   - ✅ `text="Generate Essay"`

3. **Strategic Button Colors (`style`):**
   - Use `primary` (blue) for standard actions.
   - Use `success` (green) to spotlight the primary recommended option (e.g. middle subscription plan or "Confirm").
   - Use `danger` (red) only for back, cancel, or delete buttons.

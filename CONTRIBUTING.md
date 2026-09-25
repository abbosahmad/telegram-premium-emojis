# Contributing to Telegram Premium Emojis

We welcome contributions from the community! Whether you are submitting newly discovered sticker/custom emoji packs, reporting bugs, or improving tools, here is how you can help.

---

## Adding New Custom Emoji Packs

If you found a high-quality Telegram custom emoji pack that works well with Telegram bots:

1. **Scan the pack** using our built-in scanner:
   ```bash
   python -m telegram_premium_emojis.scanner YourPackName --token YOUR_BOT_TOKEN --format json --out my_pack.json
   ```
2. Verify that the pack is public and that emojis render properly.
3. Open a Pull Request adding the pack to `catalog/curated_packs.json` and updating `catalog/all_emojis.json`.

---

## Development & Testing

1. Clone the repository:
   ```bash
   git clone https://github.com/AbbosPC/telegram-premium-emojis.git
   cd telegram-premium-emojis
   ```

2. Install dependencies:
   ```bash
   pip install -e .
   pip install pytest aiohttp aiogram
   ```

3. Run unit tests:
   ```bash
   pytest tests -v
   ```

4. Run code validator:
   ```bash
   python -m telegram_premium_emojis.validator .
   ```

---

## Code of Conduct
Please be polite, constructive, and respectful to all contributors.

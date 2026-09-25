"""
Aiogram 3 Example: Basic Message with Telegram Premium Custom Emojis
"""
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from telegram_premium_emojis import tg_emoji, CommonIcons, validation_badge

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    # Constructing a message with custom premium emojis and fallback unicode icons
    text = (
        f"<b>{tg_emoji(CommonIcons.CROWN, '👑')} Welcome to Premium Bot!</b>\n\n"
        f"This bot utilizes official Telegram Custom Emojis:\n"
        f"• {tg_emoji(CommonIcons.DIAMOND, '💎')} <b>Credits:</b> 100 tokens\n"
        f"• {tg_emoji(CommonIcons.STAR, '⭐️')} <b>Tier:</b> Pro Member\n"
        f"• {tg_emoji(CommonIcons.LIGHTNING, '⚡️')} <b>Speed:</b> Instant Priority\n\n"
        f"{validation_badge('success', 'Your subscription is active and verified!')}"
    )

    await message.answer(text)


async def main():
    print("Bot is starting...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

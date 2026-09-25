"""
Aiogram 3 Example: Inline Buttons with Custom Emoji Icons & Button Styles
"""
import os
import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.default import DefaultBotProperties

from telegram_premium_emojis import (
    CommonIcons,
    build_inline_button,
    TelegramCard
)

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


def get_payment_menu():
    builder = InlineKeyboardBuilder()

    # Rule: Keep button text clean! Do not put unicode emojis inside text
    # when icon_custom_emoji_id is already passed.
    builder.row(
        build_inline_button(
            text="Starter Pack (18 tokens)",
            callback_data="buy_starter",
            icon_custom_emoji_id=CommonIcons.DIAMOND,
            style="primary"
        )
    )
    builder.row(
        build_inline_button(
            text="Pro Unlimited Plan",
            callback_data="buy_pro",
            icon_custom_emoji_id=CommonIcons.STAR,
            style="success"  # Highlights the recommended plan in green
        )
    )
    builder.row(
        build_inline_button(
            text="Back",
            callback_data="nav_back",
            icon_custom_emoji_id=CommonIcons.BACK,
            style="danger"  # Back / cancel buttons in red/soft red
        )
    )

    return builder.as_markup()


@dp.message(Command("pricing"))
async def pricing_handler(message: types.Message):
    card = (
        TelegramCard()
        .set_title("Subscription & Token Plans", icon_id=CommonIcons.CROWN)
        .add_line("Choose a plan that fits your workflow.", icon_id=CommonIcons.SPARKLES)
        .add_line("Tokens never expire and can be used anytime.", icon_id=CommonIcons.LOCK)
        .add_line("Instant card payments via Payme & Click.", icon_id=CommonIcons.CARD)
        .with_spacer()
        .build()
    )

    await message.answer(card, reply_markup=get_payment_menu())


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

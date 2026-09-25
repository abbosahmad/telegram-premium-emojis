"""
Aiogram 3 Example: Modern Card UI with Invisible Spacers & Expandable Signature
"""
import os
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.client.default import DefaultBotProperties

from telegram_premium_emojis import (
    TelegramCard,
    CommonIcons,
    build_inline_button
)

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)
dp = Dispatcher()


@dp.message(Command("card_demo"))
async def card_demo_handler(message: types.Message):
    # Constructing a complete Telegram Card conforming to modern design standards
    card = (
        TelegramCard()
        .set_title("Course Work Document Ready!", icon_id=CommonIcons.SUCCESS)
        .add_line("Topic: Machine Learning in Healthcare", icon_id=CommonIcons.DOCUMENT)
        .add_line("Pages: 32 pages (Times New Roman, 14pt)", icon_id=CommonIcons.EDIT)
        .add_line("Plagiarism Check: 94% Unique (Clean)", icon_id=CommonIcons.LIGHTNING)
        .add_line("Storage: Saved in your cloud storage for 30 days", icon_id=CommonIcons.FOLDER)
        .with_spacer(True)  # Forces full-width rendering across mobile and desktop
        .set_signature("Processed by @osonpdfrobot • Fast, Reliable, Premium", expandable=True)
        .build()
    )

    builder = InlineKeyboardBuilder()
    builder.row(
        build_inline_button(
            text="Download Word (.docx)",
            callback_data="download_docx",
            icon_custom_emoji_id=CommonIcons.DOWNLOAD,
            style="success"
        ),
        build_inline_button(
            text="Download PDF",
            callback_data="download_pdf",
            icon_custom_emoji_id=CommonIcons.DOCUMENT,
            style="primary"
        )
    )
    builder.row(
        build_inline_button(
            text="Main Menu",
            callback_data="main_menu",
            icon_custom_emoji_id=CommonIcons.HOME
        )
    )

    await message.answer(card, reply_markup=builder.as_markup())


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

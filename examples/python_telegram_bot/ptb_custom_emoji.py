"""
Python-Telegram-Bot (PTB) Example: Custom Emojis in HTML Parse Mode
"""
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from telegram_premium_emojis import TelegramCard, CommonIcons

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    card = (
        TelegramCard()
        .set_title("Welcome to PTB Custom Emoji Demo", icon_id=CommonIcons.SPARKLES)
        .add_line("This bot demonstrates custom emojis with python-telegram-bot.", icon_id=CommonIcons.INFO)
        .add_line("Seamless HTML rendering for modern bot interfaces.", icon_id=CommonIcons.STAR)
        .with_spacer()
        .set_signature("Built with telegram-premium-emojis", expandable=True)
        .build()
    )

    keyboard = [
        [
            InlineKeyboardButton("Documentation", url="https://github.com/AbbosPC/telegram-premium-emojis"),
            InlineKeyboardButton("Catalog", url="https://github.com/AbbosPC/telegram-premium-emojis/tree/main/catalog")
        ]
    ]

    await update.message.reply_text(
        text=card,
        parse_mode=ParseMode.HTML,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("PTB Bot started...")
    app.run_polling()


if __name__ == "__main__":
    main()

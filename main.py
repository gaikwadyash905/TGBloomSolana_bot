import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Load the .env file
load_dotenv()

# Fetch the bot token from the environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Wallet and Status
    wallet_address = "7wp112h97RY5yo5uyaxhsFY98Tm63KH12MNSJQq4uJC8"
    balance = "0 SOL (USD $0)"
    status = "🔴 You currently have no SOL in your wallet.\nTo start trading, please deposit SOL to your address."

    # Resources Section
    resources = (
        "[📖 Bloom Guides](https://example.com)\n"
        "[🔔 Bloom X](https://example.com)\n"
        "[🌐 Bloom Website](https://example.com)\n"
        "[💛 Bloom Portal](https://example.com)"
    )

    # Buttons Section
    keyboard = [
        [InlineKeyboardButton("Positions", callback_data='positions')],
        [InlineKeyboardButton("LP Sniper", callback_data='lp_sniper')],
        [InlineKeyboardButton("Copy Trade", callback_data='copy_trade')],
        [InlineKeyboardButton("AFK Mode", callback_data='afk_mode')],
        [InlineKeyboardButton("Limit Orders", callback_data='limit_orders')],
        [InlineKeyboardButton("Withdraw", callback_data='withdraw')],
        [InlineKeyboardButton("Settings", callback_data='settings')],
        [InlineKeyboardButton("Refresh", callback_data='refresh')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    # Message Content
    message = (
        f"Welcome to Bloom! 🌸\n\n"
        f"Let your trading journey *blossom* with us!\n\n"
        f"💜 *Your Solana Wallet Address:*\n"
        f"`{wallet_address}`\n"
        f"*Balance:* {balance}\n\n"
        f"{status}\n\n"
        f"📚 *Resources:*\n{resources}\n\n"
        f"Last updated: 15:10:03.318"
    )

    await update.message.reply_text(
        message,
        parse_mode='Markdown',
        reply_markup=reply_markup
    )

# Callback for button clicks
async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"You clicked: {query.data}")

def main() -> None:
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(button_click))

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()

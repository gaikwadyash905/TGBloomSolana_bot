from .base_dashboard import BaseDashboard
from telegram import InlineKeyboardButton

class MainDashboard(BaseDashboard):
    """Handles the main dashboard UI and functionality."""

    async def show(self, update, context):
        self.current_dashboard = "main"
        wallet_address = self.wallet_generator.public_key
        balance = "0 SOL (USD $0)"
        status = "🔴 You currently have no SOL in your wallet.\nTo start trading, please deposit SOL to your address."

        keyboard = [
            [InlineKeyboardButton("👜Positions", callback_data="positions"), InlineKeyboardButton("🏹LP Sniper", callback_data="lp_sniper")],
            [InlineKeyboardButton("🤖Copy Trade", callback_data="copy_trade"), InlineKeyboardButton("💤AFK Mode", callback_data="afk_mode")],
            [InlineKeyboardButton("Withdraw", callback_data="withdraw"), InlineKeyboardButton("⚙️Settings", callback_data="settings")],
            [InlineKeyboardButton("🚮Close", callback_data="close"), InlineKeyboardButton("♻️Refresh", callback_data="refresh")],
        ]
        reply_markup = self.create_reply_markup(keyboard)

        last_updated = self.get_us_time()

        message = (
            f"Welcome to Bloom! 🌸\n\n"
            f"Let your trading journey *blossom* with us!\n\n"
            f"💜 *Your Solana Wallet Address:*\n"
            f"`{wallet_address}`\n"
            f"*Balance:* {balance}\n\n"
            f"{status}\n\n"
            f"📚 *Resources:*\n"
            f"[📖 Bloom Guides](https://example.com)\n"
            f"[🔔 Bloom X](https://example.com)\n"
            f"[🌐 Bloom Website](https://example.com)\n"
            f"[💛 Bloom Portal](https://example.com)\n\n"
            f"🕒 Last updated: {last_updated}"
        )

        if update.callback_query:
            await update.callback_query.message.edit_text(message, parse_mode="Markdown", reply_markup=reply_markup)
        else:
            await update.message.reply_text(message, parse_mode="Markdown", reply_markup=reply_markup)

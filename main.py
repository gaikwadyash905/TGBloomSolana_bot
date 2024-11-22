import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from solders.keypair import Keypair
import base58

# Load the .env file
load_dotenv()

# Fetch the bot token from the environment variable
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


# Solana Wallet Generator Class
class SolanaKeyGenerator:
    """Handles the generation and management of Solana keypairs."""

    def __init__(self):
        self.keypair = None

    def generate_new_keypair(self):
        """Generate a new Solana keypair."""
        self.keypair = Keypair()
        return self

    @property
    def public_key(self):
        """Get public key (address) as base58 string."""
        return str(self.keypair.pubkey())

    @property
    def private_key_base58(self):
        """Get private key as base58 string."""
        return base58.b58encode(self.keypair.secret()).decode("ascii")


# Function to generate a new Solana wallet
def generate_solana_wallet():
    """Generate and return a new Solana wallet."""
    generator = SolanaKeyGenerator()
    generator.generate_new_keypair()
    return generator


# DashboardManager: Manages the navigation between different dashboards
class DashboardManager:
    """Manages dashboard UI and navigation."""

    def __init__(self):
        self.wallet_generator = generate_solana_wallet()

    async def show_main_dashboard(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Displays the main dashboard."""
        wallet_address = self.wallet_generator.public_key

        # Wallet and Status
        balance = "0 SOL (USD $0)"
        status = "🔴 You currently have no SOL in your wallet.\nTo start trading, please deposit SOL to your address."

        # Buttons for main dashboard
        keyboard = [
            [InlineKeyboardButton("Positions", callback_data='positions'), InlineKeyboardButton("LP Sniper", callback_data='lp_sniper')],
            [InlineKeyboardButton("Copy Trade", callback_data='copy_trade'), InlineKeyboardButton("AFK Mode", callback_data='afk_mode')],
            [InlineKeyboardButton("Limit Orders", callback_data='limit_orders'), InlineKeyboardButton("Referrals", callback_data='referrals')],
            [InlineKeyboardButton("Withdraw", callback_data='withdraw'), InlineKeyboardButton("Settings", callback_data='settings')],
            [InlineKeyboardButton("Close", callback_data='close'), InlineKeyboardButton("Refresh", callback_data='refresh')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        # Main dashboard content
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
            f"Last updated: 15:10:03.318"
        )

        if update.callback_query:
            await update.callback_query.message.edit_text(message, parse_mode="Markdown", reply_markup=reply_markup)
        else:
            await update.message.reply_text(message, parse_mode="Markdown", reply_markup=reply_markup)

    async def show_settings_dashboard(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Displays the settings dashboard."""
        # Buttons for settings dashboard
        keyboard = [
            [InlineKeyboardButton("Fee", callback_data='fee'), InlineKeyboardButton("Wallets", callback_data='wallets')],
            [InlineKeyboardButton("Buy Presets", callback_data='buy_presets'), InlineKeyboardButton("Sell Presets", callback_data='sell_presets')],
            [InlineKeyboardButton("Spot Presets", callback_data='spot_presets'), InlineKeyboardButton("Sniper Presets", callback_data='sniper_presets')],
            [InlineKeyboardButton("Degen Mode", callback_data='degen_mode'), InlineKeyboardButton("MEV Protect", callback_data='mev_protect')],
            [InlineKeyboardButton("Buy: node", callback_data='buy_node'), InlineKeyboardButton("Sell: node", callback_data='sell_node')],
            [InlineKeyboardButton("Buy Slippage: 20%", callback_data='buy_slippage'), InlineKeyboardButton("Sell Slippage: 15%", callback_data='sell_slippage')],
            [InlineKeyboardButton("Back", callback_data='back'), InlineKeyboardButton("Close", callback_data='close')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        # Settings dashboard content
        message = (
            f"🌸 *Bloom Settings*\n\n"
            f"🟢 : The feature/mode is turned *ON*\n"
            f"🔴 : The feature/mode is turned *OFF*\n\n"
            f"[Learn More!](https://example.com)\n\n"
            f"🕒 Last updated: 18:53:13.881"
        )

        await update.callback_query.message.edit_text(message, parse_mode="Markdown", reply_markup=reply_markup)

    async def handle_button_click(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handles button click events and navigates between dashboards."""
        query = update.callback_query

        if query.data == "settings":
            await self.show_settings_dashboard(update, context)
        elif query.data == "back":
            await self.show_main_dashboard(update, context)
        elif query.data == "close":
            await query.message.delete()
        else:
            await query.answer()
            await query.edit_message_text(text=f"You clicked: {query.data}")


# Main function to initialize and run the bot
def main() -> None:
    """Run the bot with structured navigation."""
    dashboard_manager = DashboardManager()

    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler('start', dashboard_manager.show_main_dashboard))
    application.add_handler(CallbackQueryHandler(dashboard_manager.handle_button_click))

    # Run the bot
    application.run_polling()


if __name__ == '__main__':
    main()

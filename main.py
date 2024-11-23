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
            [InlineKeyboardButton("Wallet", callback_data='wallet'), InlineKeyboardButton("Settings", callback_data='settings')],
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

    async def show_afk_dashboard(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Displays the AFK Mode (ZFK Mode) dashboard."""
        wallet_address = self.wallet_generator.public_key

        # Buttons for AFK Mode dashboard
        keyboard = [
            [InlineKeyboardButton("Add new config", callback_data='add_config')],
            [InlineKeyboardButton("Pause All", callback_data='pause_all'), InlineKeyboardButton("Start All", callback_data='start_all')],
            [InlineKeyboardButton("Back", callback_data='back'), InlineKeyboardButton("Refresh", callback_data='refresh')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        # AFK Mode dashboard content
        message = (
            f"🌸 *Bloom AFK*\n\n"
            f"💡 Run your bot while you are away!\n\n"
            f"AFK Wallet:\n"
            f"→ `W1: {wallet_address}`\n\n"
            f"🟢 AFK mode is *active*\n"
            f"🔴 AFK mode is *inactive*\n\n"
            f"⚠️ Please wait 10 seconds after each change for it to take effect.\n\n"
            f"⚠️ Changing your Default wallet? Remember to remake your tasks to use the new wallet for future transactions.\n\n"
            f"🕒 Last updated: 19:40:32.861"
        )

        await update.callback_query.message.edit_text(message, parse_mode="Markdown", reply_markup=reply_markup)

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

    async def show_position_dashboard(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Display the position settings dashboard."""
        # Buttons for position dashboard
        keyboard = [
            [InlineKeyboardButton("Min Value: N/A Sol", callback_data='min_val'), InlineKeyboardButton("Refresh", callback_data='refresh')],
            [InlineKeyboardButton("HomePage", callback_data='homepage'), InlineKeyboardButton("Delete", callback_data='delete')]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        # Position dashboard content
        message = (
            f"🌸 Bloom Positions"
            f"No open positions yet!"
            f"Start your trading journey by pasting a contract address in chat."
            f"🕒 Last updated: 10:32:20.564"
        )

        await update.callback_query.message.edit_text(message, parse_mode="Markdown", reply_markup=reply_markup)

    async def show_sniper_dashboard(self, update: Update, context: ContextTypes.DEFAULT_TYPE)-> None:
        """Display the sniper dashboard."""
        # Buttons for sniper dashboard
        keyboard = [
            [InlineKeyboardButton("Sniper Wallets:0", callback_data='sniper_wallet'), InlineKeyboardButton("Create Task", callback_data='create_task')],
            [InlineKeyboardButton("Back", callback_data='back'), InlineKeyboardButton("Refresh", callback_data='refresh')],
            InlineKeyboardButton("Close", callback_data='close')
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        # sniper dashboard content
        message = (
            f"🌸 Bloom Positions"
            f"🧐 No active sniper tasks!"
            f"📖 Learn More!"
            f"🕒 Last updated: 13:50:13.549"
        )

        await update.callback_query.message.edit_text(message, parse_mode="Markdown", reply_markup=reply_markup)

    async def handle_button_click(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """Handles button click events and navigates between dashboards."""
        query = update.callback_query

        if query.data == "afk_mode":
            await self.show_afk_dashboard(update, context)
        elif query.data == "settings":
            await self.show_settings_dashboard(update, context)
        elif query.data == "back":
            await self.show_main_dashboard(update, context)
        elif query.data == "homepage":
            await self.show_main_dashboard(update, context)
        elif query.data == "close":
            await query.message.delete()
        elif query.data == "positions":
            await self.show_position_dashboard(update, context)
        elif query.data == "lp_sniper":
            await self.show_sniper_dashboard(update, context)
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

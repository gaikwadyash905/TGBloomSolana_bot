from .base_dashboard import BaseDashboard
from telegram import InlineKeyboardButton


class SettingDashboard(BaseDashboard):
    """Handles the Setting dashboard."""

    def __init__(self, wallet_generator, time_utils, main_dashboard):
        super().__init__(wallet_generator, time_utils)
        self.main_dashboard = main_dashboard

    async def show(self, update, context):
        """Displays the Setting dashboard."""
        self.current_dashboard = "setting"
        wallet_address = self.wallet_generator.public_key

        keyboard = [
            [InlineKeyboardButton("Fee", callback_data='feesetting'), InlineKeyboardButton("💰Wallet", callback_data='wallet')],
            [InlineKeyboardButton("Buy Presets", callback_data='buy_presets'), InlineKeyboardButton("Sell Presets", callback_data='sell_presets')],
            [InlineKeyboardButton("Spot Presets", callback_data='spot_presets'), InlineKeyboardButton("Sniper Presets", callback_data='sniper_presets')],
            [InlineKeyboardButton("Degen Mode", callback_data='degen_mode'), InlineKeyboardButton("MEV Protect", callback_data='mev_protect')],
            [InlineKeyboardButton("Buy: node", callback_data='buy_node'), InlineKeyboardButton("Sell: node", callback_data='sell_node')],
            [InlineKeyboardButton("Buy Slippage: 20%", callback_data='buy_slippage'), InlineKeyboardButton("Sell Slippage: 15%", callback_data='sell_slippage')],
            [InlineKeyboardButton("Back", callback_data='back_to_main'), InlineKeyboardButton("🚮Close", callback_data='delete')],
        ]

        reply_markup = self.create_reply_markup(keyboard)

        last_updated = self.get_us_time()

        message = (
            f"🌸 *Bloom Settings*\n\n"
            f"🟢 : The feature/mode is turned *ON*\n"
            f"🔴 : The feature/mode is turned *OFF*\n\n"
            f"[Learn More!](https://example.com)\n\n"
            f"🕒 Last updated: {last_updated}"
        )

        await update.callback_query.message.edit_text(message, parse_mode="Markdown", reply_markup=reply_markup)

    async def handle_button_click(self, update, context):
        """Handles button clicks within the setting dashboard."""
        query = update.callback_query

        if query.data == "back_to_main":
            # Navigate back to the main dashboard
            await self.main_dashboard.show(update, context)
        elif query.data == "refresh":
            # Refresh the current dashboard
            await self.show(update, context)
        elif query.data == "delete":
             await query.message.delete()
        else:
            await query.answer()

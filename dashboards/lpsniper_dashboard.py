from .base_dashboard import BaseDashboard
from telegram import InlineKeyboardButton


class LpSniperDashboard(BaseDashboard):
    """Handles the LpSniper dashboard."""

    def __init__(self, wallet_generator, time_utils, main_dashboard):
        super().__init__(wallet_generator, time_utils)
        self.main_dashboard = main_dashboard

    async def show(self, update, context):
        """Displays the LpSniper dashboard."""
        self.current_dashboard = "lpsniper"
        wallet_address = self.wallet_generator.public_key

        keyboard = [
            [InlineKeyboardButton("Sniper Wallets:0", callback_data='sniper_wallet'), InlineKeyboardButton("Create Task", callback_data='create_task')],
            [InlineKeyboardButton("Back", callback_data='back_to_main'), InlineKeyboardButton("♻️Refresh", callback_data='refresh')],
            [InlineKeyboardButton("🚮Close", callback_data='delete')]
        ]

        reply_markup = self.create_reply_markup(keyboard)

        last_updated = self.get_us_time()

        message = (
            f"🌸 Bloom Positions\n\n"
            f"🧐 No active sniper tasks!\n\n"
            f"📖 Learn More!\n\n"
            f"🕒 Last updated: {last_updated}\n\n"
        )

        await update.callback_query.message.edit_text(message, parse_mode="Markdown", reply_markup=reply_markup)

    async def handle_button_click(self, update, context):
        """Handles button clicks within the lpsniper dashboard."""
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

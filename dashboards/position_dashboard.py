from .base_dashboard import BaseDashboard
from telegram import InlineKeyboardButton


class PositionDashboard(BaseDashboard):
    """Handles the Position dashboard."""

    def __init__(self, wallet_generator, time_utils, main_dashboard):
        super().__init__(wallet_generator, time_utils)
        self.main_dashboard = main_dashboard

    async def show(self, update, context):
        """Displays the Position dashboard."""
        self.current_dashboard = "position"
        wallet_address = self.wallet_generator.public_key

        keyboard = [
            [InlineKeyboardButton("Min Value: N/A Sol", callback_data='min_val'), InlineKeyboardButton("♻️Refresh", callback_data='refresh')],
            [InlineKeyboardButton("HomePage", callback_data='back_to_main'), InlineKeyboardButton("Delete", callback_data='delete')]
        ]
        reply_markup = self.create_reply_markup(keyboard)

        last_updated = self.get_us_time()

        message = (
            f"🌸 Bloom Positions\n\n"
            f"No open positions yet!\n\n"
            f"Start your trading journey by pasting a contract address in chat.\n\n"
            f"🕒 Last updated: {last_updated}\n\n"
        )

        await update.callback_query.message.edit_text(message, parse_mode="Markdown", reply_markup=reply_markup)

    async def handle_button_click(self, update, context):
        """Handles button clicks within the Position dashboard."""
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

from .base_dashboard import BaseDashboard
from telegram import InlineKeyboardButton


class AfkDashboard(BaseDashboard):
    """Handles the AFK Mode (ZFK Mode) dashboard."""

    def __init__(self, wallet_generator, time_utils, main_dashboard):
        super().__init__(wallet_generator, time_utils)
        self.main_dashboard = main_dashboard

    async def show(self, update, context):
        """Displays the AFK dashboard."""
        self.current_dashboard = "afk"
        wallet_address = self.wallet_generator.public_key

        keyboard = [
            [InlineKeyboardButton("Add new config", callback_data="add_config")],
            [InlineKeyboardButton("Pause All", callback_data="pause_all"), InlineKeyboardButton("Start All", callback_data="start_all")],
            [InlineKeyboardButton("Back", callback_data="back_to_main"), InlineKeyboardButton("♻️Refresh", callback_data="refresh")],
        ]
        reply_markup = self.create_reply_markup(keyboard)

        last_updated = self.get_us_time()

        message = (
            f"🌸 *Bloom AFK*\n\n"
            f"💡 Run your bot while you are away!\n\n"
            f"AFK Wallet:\n"
            f"→ `W1: {wallet_address}`\n\n"
            f"🟢 AFK mode is *active*\n"
            f"🔴 AFK mode is *inactive*\n\n"
            f"⚠️ Please wait 10 seconds after each change for it to take effect.\n\n"
            f"⚠️ Changing your Default wallet? Remember to remake your tasks to use the new wallet for future transactions.\n\n"
            f"🕒 Last updated: {last_updated}"
        )

        await update.callback_query.message.edit_text(message, parse_mode="Markdown", reply_markup=reply_markup)

    async def handle_button_click(self, update, context):
        """Handles button clicks within the AFK dashboard."""
        query = update.callback_query

        if query.data == "back_to_main":
            # Navigate back to the main dashboard
            await self.main_dashboard.show(update, context)
        elif query.data == "refresh":
            # Refresh the current dashboard
            await self.show(update, context)
        else:
            await query.answer()

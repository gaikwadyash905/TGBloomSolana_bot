from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config import TOKEN
from utils.solana_keygen import generate_solana_wallet
from utils.time_utils import get_us_time
from dashboards.main_dashboard import MainDashboard

def main():
    """Run the bot."""
    wallet_generator = generate_solana_wallet()
    time_utils = get_us_time
    main_dashboard = MainDashboard(wallet_generator, time_utils)

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", main_dashboard.show_main_dashboard))
    application.add_handler(CallbackQueryHandler(main_dashboard.show_main_dashboard, pattern="main"))

    application.run_polling()

if __name__ == "__main__":
    main()

from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config import TOKEN
from utils.solana_keygen import generate_solana_wallet
from utils.time_utils import get_us_time
from dashboards.main_dashboard import MainDashboard
from dashboards.afk_dashboard import AfkDashboard

def main():
    """Run the bot."""
    wallet_generator = generate_solana_wallet()
    time_utils = get_us_time
    main_dashboard = MainDashboard(wallet_generator, time_utils)
    afk_dashboard = AfkDashboard(wallet_generator, time_utils, main_dashboard)

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", main_dashboard.show))
    application.add_handler(CallbackQueryHandler(main_dashboard.show, pattern="main"))
    
    application.add_handler(CallbackQueryHandler(afk_dashboard.show, pattern="afk_mode"))
    application.add_handler(CallbackQueryHandler(afk_dashboard.handle_button_click, pattern="afk_mode|back_to_main|refresh"))

    application.run_polling()


if __name__ == "__main__":
    main()
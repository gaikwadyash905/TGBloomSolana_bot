from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from config import TOKEN
from utils.solana_keygen import generate_solana_wallet
from utils.time_utils import get_us_time
from dashboards.main_dashboard import MainDashboard
from dashboards.afk_dashboard import AfkDashboard
from dashboards.position_dashboard import PositionDashboard
from dashboards.trade_dashboard import TradeDashboard
from dashboards.withdraw_dashboard import WithdrawDashboard
from dashboards.setting_dashboard import SettingDashboard
from dashboards.lpsniper_dashboard import LpSniperDashboard

def main():
    """Run the bot."""
    wallet_generator = generate_solana_wallet()
    time_utils = get_us_time

    main_dashboard = MainDashboard(wallet_generator, time_utils)
    afk_dashboard = AfkDashboard(wallet_generator, time_utils, main_dashboard)
    position_dashboard = PositionDashboard(wallet_generator, time_utils, main_dashboard)
    trade_dashboard = TradeDashboard(wallet_generator, time_utils, main_dashboard)
    withdraw_dashboard = WithdrawDashboard(wallet_generator, time_utils, main_dashboard)
    setting_dashboard = SettingDashboard(wallet_generator, time_utils, main_dashboard)
    lpsniper_dashboard = LpSniperDashboard(wallet_generator, time_utils, main_dashboard)

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", main_dashboard.show))
    application.add_handler(CallbackQueryHandler(main_dashboard.show, pattern="main"))

    application.add_handler(CallbackQueryHandler(afk_dashboard.show, pattern="afk_mode"))
    application.add_handler(CallbackQueryHandler(afk_dashboard.handle_button_click, pattern="afk_mode|back_to_main|refresh"))

    application.add_handler(CallbackQueryHandler(position_dashboard.show, pattern="positions"))
    application.add_handler(CallbackQueryHandler(position_dashboard.handle_button_click, pattern="back_to_main|refresh"))

    application.add_handler(CallbackQueryHandler(trade_dashboard.show, pattern="copy_trade"))
    application.add_handler(CallbackQueryHandler(trade_dashboard.handle_button_click, pattern="back_to_main|refresh"))

    application.add_handler(CallbackQueryHandler(withdraw_dashboard.show, pattern="withdraw"))
    application.add_handler(CallbackQueryHandler(withdraw_dashboard.handle_button_click, pattern="back_to_main|refresh"))

    application.add_handler(CallbackQueryHandler(setting_dashboard.show, pattern="settings"))
    application.add_handler(CallbackQueryHandler(setting_dashboard.handle_button_click, pattern="back_to_main|refresh"))

    application.add_handler(CallbackQueryHandler(lpsniper_dashboard.show, pattern="lp_sniper"))
    application.add_handler(CallbackQueryHandler(lpsniper_dashboard.handle_button_click, pattern="back_to_main|refresh"))


    application.run_polling()


if __name__ == "__main__":
    main()
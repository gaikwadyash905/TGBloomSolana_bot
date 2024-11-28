from telegram import InlineKeyboardMarkup

class BaseDashboard:
    """
    Base class for managing dashboard functionalities.

    This class serves as a foundation for creating and managing interactive dashboards.
    It provides utilities for wallet generation, time-related functionality, and
    creating inline keyboards for Telegram bots.
    """

    def __init__(self, wallet_generator, time_utils):
        """
        Initialize the BaseDashboard instance.

        Args:
            wallet_generator (callable): A wallet generator function or object, 
                                         typically used for creating new wallets.
            time_utils (callable): A utility function to retrieve the current time,
                                   such as a function to get US Eastern Time.

        Attributes:
            wallet_generator (callable): Stores the wallet generator utility.
            get_us_time (callable): Stores the time utility function.
            current_dashboard (str): Tracks the current active dashboard. Defaults to "main".

        Example:
            >>> dashboard = BaseDashboard(wallet_generator=generate_solana_wallet, time_utils=get_us_time)
            >>> dashboard.current_dashboard
            'main'
        """
        self.wallet_generator = wallet_generator
        self.get_us_time = time_utils
        self.current_dashboard = "main"

    def create_reply_markup(self, keyboard):
        """
        Create an inline keyboard markup for Telegram bots.

        This method generates an `InlineKeyboardMarkup` object using the provided
        keyboard layout, which is structured as a list of button rows. The resulting
        markup is used to create interactive Telegram bot interfaces.

        Args:
            keyboard (list[list[telegram.InlineKeyboardButton]]): A 2D list of 
                                                                  InlineKeyboardButton objects representing 
                                                                  the keyboard layout.

        Returns:
            InlineKeyboardMarkup: The generated inline keyboard markup.

        Example:
            >>> from telegram import InlineKeyboardButton
            >>> keyboard = [[InlineKeyboardButton("Button 1", callback_data="1"),
                             InlineKeyboardButton("Button 2", callback_data="2")]]
            >>> dashboard = BaseDashboard(wallet_generator=None, time_utils=None)
            >>> reply_markup = dashboard.create_reply_markup(keyboard)
            >>> type(reply_markup)
            <class 'telegram.inline.inlinekeyboardmarkup.InlineKeyboardMarkup'>
        """
        return InlineKeyboardMarkup(keyboard)

# TGBloomSolana_bot 🌸

A sophisticated Telegram bot for Solana trading, copy trading, and wallet management. Built with Python and the python-telegram-bot library, this bot provides an intuitive dashboard interface for managing Solana operations.

## Features

- **🌸 Main Dashboard**: Central hub with wallet information and balance display
- **👜 Position Management**: Track and manage your trading positions
- **🏹 LP Sniper**: Liquidity pool sniping functionality
- **🤖 Copy Trading**: Follow and copy successful traders
- **💤 AFK Mode**: Automated trading while away
- **💰 Wallet Management**: Generate and manage Solana wallets
- **⚙️ Settings**: Configurable trading parameters and preferences
- **💸 Withdraw**: Easy SOL withdrawal functionality

## Project Structure

```
TGBloomSolana_bot/
├── main.py                     # Main bot application
├── config.py                   # Configuration management
├── requirements.txt            # Python dependencies
├── .env.sample                 # Environment variables template
├── utils/
│   ├── solana_keygen.py       # Solana wallet generation utilities
│   └── time_utils.py          # Time and timezone utilities
└── dashboards/
    ├── base_dashboard.py      # Base dashboard class
    ├── main_dashboard.py      # Main dashboard interface
    ├── afk_dashboard.py       # AFK mode management
    ├── position_dashboard.py  # Position tracking
    ├── trade_dashboard.py     # Copy trading interface
    ├── withdraw_dashboard.py  # Withdrawal management
    ├── setting_dashboard.py   # Bot settings
    └── lpsniper_dashboard.py  # LP sniping functionality
```

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/TGBloomSolana_bot.git
   cd TGBloomSolana_bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   ```bash
   cp .env.sample .env
   ```
   Edit `.env` and add your Telegram bot token:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```

4. **Run the bot**
   ```bash
   python main.py
   ```

## Dependencies

- **python-telegram-bot**: Telegram bot framework
- **solders**: Solana Python SDK for keypair generation
- **base58**: Base58 encoding/decoding
- **python-dotenv**: Environment variable management
- **pymongo**: MongoDB driver (for future database integration)
- **pytz**: Timezone handling

## Usage

### Starting the Bot

Send `/start` to your bot in Telegram to access the main dashboard.

### Dashboard Navigation

The bot uses inline keyboards for navigation:

- **Main Dashboard**: Overview of wallet balance and quick access to features
- **Positions**: View and manage current trading positions
- **LP Sniper**: Set up liquidity pool sniping tasks
- **Copy Trade**: Configure copy trading settings
- **AFK Mode**: Set up automated trading parameters
- **Settings**: Configure slippage, fees, and trading preferences
- **Withdraw**: Manage SOL withdrawals

### Key Components

#### Wallet Generation
The bot automatically generates a new Solana wallet using the [`generate_solana_wallet`](utils/solana_keygen.py) function from [utils/solana_keygen.py](utils/solana_keygen.py).

#### Time Management
All timestamps use US Eastern Time via the [`get_us_time`](utils/time_utils.py) function from [utils/time_utils.py](utils/time_utils.py).

#### Dashboard System
Each dashboard inherits from [`BaseDashboard`](dashboards/base_dashboard.py) in [dashboards/base_dashboard.py](dashboards/base_dashboard.py), providing consistent functionality for:
- Inline keyboard creation
- Time display
- Wallet address access

## Configuration

### Environment Variables

Create a `.env` file based on `.env.sample`:

```env
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

### Bot Settings

The bot includes configurable settings for:
- Buy/Sell slippage percentages
- Trading node selection
- MEV protection
- Fee management
- Degen mode

## Development

### Adding New Dashboards

1. Create a new dashboard class inheriting from [`BaseDashboard`](dashboards/base_dashboard.py)
2. Implement `show()` and `handle_button_click()` methods
3. Register handlers in [main.py](main.py)

Example:
```python
from .base_dashboard import BaseDashboard
from telegram import InlineKeyboardButton

class NewDashboard(BaseDashboard):
    def __init__(self, wallet_generator, time_utils, main_dashboard):
        super().__init__(wallet_generator, time_utils)
        self.main_dashboard = main_dashboard

    async def show(self, update, context):
        # Dashboard display logic
        pass

    async def handle_button_click(self, update, context):
        # Button click handling
        pass
```

### Code Structure

- **[main.py](main.py)**: Application entry point and handler registration
- **[config.py](config.py)**: Configuration management with environment variables
- **[utils/](utils/)**: Utility functions for wallet generation and time management
- **[dashboards/](dashboards/)**: Dashboard classes for different bot features

## Security Considerations

- Private keys are generated locally and handled securely
- Environment variables are used for sensitive configuration
- The `.env` file is git-ignored to prevent token exposure

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## Support

For support and questions:
- Create an issue on GitHub
- Check the documentation links in the bot interface

## Disclaimer

This bot is for educational and development purposes. Always exercise caution when trading cryptocurrencies and never invest more than you can afford to lose.

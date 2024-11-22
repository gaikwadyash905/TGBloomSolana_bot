import os
from dotenv import load_dotenv
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Load the .env file
load_dotenv()

def main() -> None:
    # Create the Application
    application = Application.builder().token(TOKEN).build()

    # Handlers

    # Run the bot
    application.run_polling()

if __name__ == '__main__':
    main()

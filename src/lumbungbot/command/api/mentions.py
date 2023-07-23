from telegram import Update, MessageEntity
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext
from telegram.ext import ContextTypes
from telegram.ext import filters

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all text messages."""
    message = update.message.text
    bot_username = context.bot.username
   
    if bot_username in message:
        await update.message.reply_text('You mentioned me!')
        


message_handler = MessageHandler(
    filters.TEXT & ~filters.COMMAND,
    handle_message
)
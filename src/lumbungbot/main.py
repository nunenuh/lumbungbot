import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def create_application():
    app = ApplicationBuilder()
    
    token = ''
    app = app.token(token).build()
    
    
    return app.run_polling()
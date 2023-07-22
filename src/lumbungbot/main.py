import logging

from command.handlers import api_handlers
from core.config import settings
from telegram.ext import ApplicationBuilder

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)


def create_application() -> ApplicationBuilder:
    app = ApplicationBuilder()
    app = app.token(settings.TOKEN).build()

    app.add_handlers(api_handlers.get_list())

    return app


if __name__ == "__main__":
    app = create_application()
    app.run_polling()

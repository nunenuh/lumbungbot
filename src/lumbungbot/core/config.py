import os

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")


class Settings:
    TOKEN: str = os.getenv("TOKEN")


settings = Settings()

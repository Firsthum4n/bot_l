import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from pydantic import SecretStr, StrictStr

load_dotenv()


class BotSettings(BaseSettings):
    """Класс скрывающий API бота"""
    tg_api_key: SecretStr = os.getenv('BOT_TOKEN', None)
    site_api_key: SecretStr = os.getenv('GPT_KEY', None)


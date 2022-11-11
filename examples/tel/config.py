import typing

from pydantic import (
    BaseSettings,
)


class Settings(BaseSettings):
    telegram_token: str  # TELEGRAM_TOKEN
    rates_url: str
    # api_version: typing.Optional[int]  #

    class Config:
        env_prefix = ""
        case_sensitive = False
        env_file = '.env'
        env_file_encoding = 'utf-8'



settings = Settings()

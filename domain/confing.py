import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = os.getenv("APP_NAME")
    debug: bool = os.getenv("DEBUG")
    version: str = os.getenv("VERSION")
    title: str = os.getenv("TITLE")
    description: str = os.getenv("DESCRIPTION")


settings = Settings()

import os
from dotenv import load_dotenv

from pathlib import Path


load_dotenv(verbose=True)


class Settings:
    PROJECT_NAME: str = "Ko_Side_Project"
    PROJECT_VERSION: str = "0.0.1"

    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER", "localhost")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB: str = os.getenv("POSTGRES_DB", "tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY: str = os.getenv("SECRET_KEY")  # new
    ALGORITHM = "HS256"  # new
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins  #new
    TEST_USER_EMAIL = "test@example.com"
    USE_SQLITE_DB: str = os.getenv("USE_SQLITE_DB")


settings = Settings()

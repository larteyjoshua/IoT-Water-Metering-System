import os
from functools import lru_cache
from typing import Optional

from pydantic import BaseSettings, AnyHttpUrl, validator
import secrets
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Settings(BaseSettings):
    PROJECT_NAME: str = "IoT Water Metering System(User Management)"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str =  secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ALGORITHM:str = os.environ.get("ALGORITHM")
    USERS_OPEN_REGISTRATION: Optional[int] = None
    ENVIRONMENT: Optional[str]

    FIRST_SUPER_ADMIN_EMAIL: str = os.environ.get("FIRST_SUPER_ADMIN_EMAIL")
    FIRST_SUPER_ADMIN_PASSWORD: str  =os.environ.get("FIRST_SUPER_ADMIN_PASSWORD")
    PHONENUMBER: str = os.environ.get("PHONENUMBER")
    
   
    SQLALCHEMY_DATABASE_URI: str = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48

    class Config:
        case_sensitive = True
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()


settings = get_settings()
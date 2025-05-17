from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Core settings
    cors_origins: str = "*"
    secret_key: str = "change me in .env"
    access_token_expire_minutes: int = 120

    # Database variables (Overwrite in .env file)
    db_user: str = "<USER>"
    db_password: str = "<PASSWORD>"
    db_address: str = "localhost"
    db_port: str = "5432"
    db_name: str = "<DATABASE>"

    # Test database variables
    test_db_user: str = "<USER-TEST>"
    test_db_password: str = "<PASSWORD-TEST>"
    test_db_address: str = "localhost"
    test_db_port: str = "5432"
    test_db_name: str = "<DATABASE-TEST>"

    # Metadata variables
    title: str = "API Template"
    description: str = "This is a simple api template for simple projects"
    version: str = "v1"
    repository: str = "https://github.com/abdurasuloff/fastapi-template"
    license_info: dict[str, str] = {"name": "MIT", "url": "https://opensource.org/licenses/MIT"}
    contact: dict[str, str] = {"name": "Abdurasulov Akbarjon", "url": "https://www.akbarjon.uz"}
    email: str = "abdurasulovcodes@gmail.com"
    year: str = "2004"

    # model_config = SettingsConfigDict(env_file=".env")
    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()

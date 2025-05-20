from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # Core settings
    cors_origins: str = "*"
    secret_key: str = "change me in .env"
    access_token_expire_minutes: int = 120

    # Database variables (Overwrite in .env file)
    db_user: str = "postgres"
    db_password: str = '1'
    db_address: str = "localhost"
    db_port: str = "5432"
    db_name: str = "ems"

    # Test database variables
    test_db_user: str = "postgres"
    test_db_password: str = "1"
    test_db_address: str = "localhost"
    test_db_port: str = "5432"
    test_db_name: str = "ems_test"

    # Metadata variables
    title: str = "API Template"
    description: str = "This is a simple api template for simple projects"
    version: str = "v1"
    repository: str = "https://github.com/abdurasuloff/fastapi-template"
    license_info: dict[str, str] = {"name": "MIT", "url": "https://opensource.org/licenses/MIT"}
    contact: dict[str, str] = {"name": "Ibrohim To'lqinov", "url": "https://github.com/ibrohim0117"}
    email: str = "ibrohim.dev.uz@gmail.com"
    year: str = "2001"

    # model_config = SettingsConfigDict(env_file=".env")
    class Config:
        env_file = ".env"

@lru_cache
def get_settings() -> Settings:
    return Settings()

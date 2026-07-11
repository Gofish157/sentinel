from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    debug: bool
    api_v1_prefix: str
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str
    model_config = SettingsConfigDict(
        env_file=".env", 
        env_file_encoding="utf-8",
        extra="ignore",
        )

settings = Settings()
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Project API"
    database_url: str
    stripe_api_key: str | None = None

    class Config:
        env_file = ".env"

settings = Settings()

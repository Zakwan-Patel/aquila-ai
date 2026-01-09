from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Aquila AI"
    environment: str = "development"
    openai_api_key: str

    class Config:
        env_file = ".env"
        extra = "forbid"


settings = Settings()

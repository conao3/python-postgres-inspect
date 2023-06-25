import pydantic


class Settings(pydantic.BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: str

    class Config:
        env_file = ".env"


settings = Settings()

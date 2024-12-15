from pydantic_settings import BaseSettings, SettingsConfigDict


class DBSettings(BaseSettings):
    pg_db: str
    pg_host: str
    pg_port: int
    pg_user: str
    pg_password: str

    model_config = SettingsConfigDict(env_file='../.env')

    def get_db_urL(self):
        return f'postgresql+asyncpg://{self.pg_user}:{self.pg_password}@{self.pg_host}:{self.pg_port}/{self.pg_db}'


settings = DBSettings()

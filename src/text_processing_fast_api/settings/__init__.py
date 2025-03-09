import urllib.parse
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL


class Settings(BaseSettings):
    """
    Application Settings
    """

    model_config = SettingsConfigDict(env_file=".env.local")

    ENVIRONMENT: str
    ENVIRONMENT_NAME: str
    IMAGE_VERSION: str

    # Database env vars
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str

    @property
    def db_dsn(self) -> URL:
        return URL.create(
            drivername="postgresql+psycopg2",
            username=self.POSTGRES_USERNAME,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            database=self.POSTGRES_DB,
        )

    @property
    def _db_password_escaped_for_alembic(self) -> str:
        """Return the password escaping the special characters as required for Alembic.
        Follows recomendation on https://docs.sqlalchemy.org/en/13/core/engines.html#database-urls.
        """
        return urllib.parse.quote_plus(self.DB_PASS).replace("%", "%%")

    @property
    def db_dsn_for_alembic(self) -> str:
        return f"postgresql+psycopg2://{self.POSTGRES_USERNAME}:{self._db_password_escaped_for_alembic}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


@lru_cache
def get_settings() -> Settings:
    return Settings()

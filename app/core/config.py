import os
from pathlib import Path

from pydantic import BaseSettings


BASE_DIR = Path(__file__).resolve().parent.parent.parent
ENV_FILE = os.path.join(BASE_DIR / ".env")


class Settings(BaseSettings):
    """Application settings class."""
    ip_address: str
    ip_port: int
    # database_url: str
    debug: bool = False
    root_path: str = ""
    postgres_db: str
    postgres_user: str
    postgres_password: str
    db_host: str
    db_port: str

    @property
    def database_url(self) -> str:
        """Get db connection url."""
        return (
            "postgresql+asyncpg://"
            f"{self.postgres_user}:{self.postgres_password}"
            f"@{self.db_host}:{self.db_port}/{self.postgres_db}"
        )

    class Config:
        env_file = ENV_FILE


settings = Settings()

from typing import Optional

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn
from tortoise import generate_config


class Settings(BaseSettings):
    env: str = "local"
    postgres_dsn: PostgresDsn = "postgres://{{cookiecutter.project_slug}}:{{cookiecutter.project_slug}}@localhost:15432/{{cookiecutter.project_slug}}"
    postgres_dsn_test: PostgresDsn = "postgres://{{cookiecutter.project_slug}}:{{cookiecutter.project_slug}}@localhost:15432/{{cookiecutter.project_slug}}_{}"
    sentry_dsn: Optional[AnyHttpUrl] = None

    # pagination
    default_limit: int = 10
    max_limit: int = 1000


settings = Settings()

db_config = generate_config(
    db_url=settings.postgres_dsn,
    app_modules={"models": ["app.models", "aerich.models"]},
)
test_db_config = generate_config(
    db_url=settings.postgres_dsn_test,
    app_modules={"models": ["app.models"]},
)

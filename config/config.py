from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class LogSettings:
    level: str
    format: str
    style: str


@dataclass
class Config:
    bot: TgBot
    log: LogSettings


def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        bot=TgBot(token=env("BOT_TOKEN"), admin_ids=env("ADMIN_IDS")),
        log=LogSettings(
            level=env("LOG_LEVEL"), format=env("LOG_FORMAT"), style=env("LOG_STYLE")
        ),
    )

import asyncio
import logging

from aiogram import Bot, Dispatcher

from config.config import Config, load_config
from handlers import admin, user


async def main():

    # Loading config
    config: Config = load_config()

    # Config logging
    logging.basicConfig(
        level=logging.getLevelName(level=config.log.level),
        format=config.log.format,
        style=config.log.style,
    )
    # Init bot and dispatcher
    bot = Bot(token=config.bot.token)
    dp = Dispatcher()

    # Include routers
    dp.include_router(admin.router)
    dp.include_router(user.router)

    # Skip updates and start polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())

# Import aiogram modules
from aiogram import Router
from aiogram.filters import CommandStart, BaseFilter
from aiogram.types import Message

# Import config, keyboard, lexicon
from config.config import Config, load_config
from keyboards.keyboards import main_keyboard
from lexicon.lexicon import LEXICON_RU


class IsAdmin(BaseFilter):
    def __init__(self, admin_ids: list[str]) -> None:
        self.admin_ids = admin_ids

    def __call__(self, message: Message) -> bool:
        return str(message.from_user.id) in self.admin_ids


router = Router()
router.message.filter(IsAdmin(load_config().bot.admin_ids))


# Greeting handler for admins
@router.message(CommandStart)
async def admin_start(message: Message):
    await message.answer(text=LEXICON_RU["admin_start"], reply_markup=main_keyboard)

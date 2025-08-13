# Import aiogram modules
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

# Import keyboard, lexicon
from keyboards.keyboards import main_keyboard
from lexicon.lexicon import LEXICON_RU

router = Router()


# Greeting handler for users
@router.message(CommandStart)
async def user_start(message: Message):
    await message.answer(text=LEXICON_RU["user_start"], reply_markup=main_keyboard)


# Handler for incorrect messages
@router.message()
async def incorrect_message(message: Message):
    await message.answer(
        text=LEXICON_RU["incorrect_message"], reply_markup=main_keyboard
    )

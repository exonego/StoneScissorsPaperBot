# Import aiogram modules
from aiogram import Router
from aiogram.filters import CommandStart, BaseFilter
from aiogram.types import Message

# Import choice
from random import choice

# Import keyboard, lexicon
from keyboards.keyboards import main_keyboard, main_buttons
from lexicon.lexicon import LEXICON_RU


class GameFilter(BaseFilter):
    def __init__(self, buttons):
        self.buttons = buttons

    def __call__(self, message: Message) -> bool:
        return message.text in self.buttons


router = Router()


# Greeting handler for users
@router.message(CommandStart())
async def user_start(message: Message):
    await message.answer(text=LEXICON_RU["user_start"], reply_markup=main_keyboard)


# Game handler
@router.message(GameFilter(main_buttons))
async def game_handler(message: Message):
    bot_choice = choice(main_buttons)
    user_win = 0

    # Draw
    if bot_choice == message.text:
        await message.answer(text=LEXICON_RU["draw"], reply_markup=main_keyboard)

    # Win or lose
    elif bot_choice == LEXICON_RU["stone"]:
        if message.text == LEXICON_RU["paper"]:
            user_win = 1
    elif bot_choice == LEXICON_RU["paper"]:
        if message.text == LEXICON_RU["scissors"]:
            user_win = 1
    elif bot_choice == LEXICON_RU["scissors"]:
        if message.text == LEXICON_RU["stone"]:
            user_win = 1

    # Result
    if user_win:
        await message.answer(text=LEXICON_RU["win"], reply_markup=main_keyboard)
    else:
        await message.answer(text=LEXICON_RU["lose"], reply_markup=main_keyboard)


# Handler for incorrect messages
@router.message()
async def incorrect_message(message: Message):
    await message.answer(
        text=LEXICON_RU["incorrect_message"], reply_markup=main_keyboard
    )

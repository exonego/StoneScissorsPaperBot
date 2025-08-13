from aiogram.utils.keyboard import ReplyKeyboardMarkup
from aiogram.types import KeyboardButton
from lexicon.lexicon import LEXICON_RU

# List of buttons
main_buttons = [LEXICON_RU["stone"], LEXICON_RU["scissors"], LEXICON_RU["paper"]]
# Buttons
stone = KeyboardButton(text=main_buttons[0])
scissors = KeyboardButton(text=main_buttons[1])
paper = KeyboardButton(text=main_buttons[2])
# Main keyboard
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[stone], [scissors], [paper]],
    resize_keyboard=True,
    input_field_placeholder="Просто нажмите кнопку",
)

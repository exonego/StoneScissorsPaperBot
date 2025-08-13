from aiogram.utils.keyboard import ReplyKeyboardMarkup
from lexicon.lexicon import LEXICON_RU

# list of buttons
main_buttons = [[LEXICON_RU["stone"]], [LEXICON_RU["scissors"]], [LEXICON_RU["paper"]]]

# main keyboard
main_keyboard = ReplyKeyboardMarkup(
    keyboard=main_buttons,
    resize_keyboard=True,
    input_field_placeholder="Просто нажмите кнопку",
)

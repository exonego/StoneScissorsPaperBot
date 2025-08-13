from aiogram.utils.keyboard import ReplyKeyboardMarkup
from lexicon.lexicon import LEXICON_RU

# main keyboard
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[[LEXICON_RU["stone"]], [LEXICON_RU["scissors"]], [LEXICON_RU["paper"]]],
    resize_keyboard=True,
    input_field_placeholder="Просто нажмите кнопку",
)

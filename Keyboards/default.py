from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

til = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('O`zbekcha'),

        ],
        [
            KeyboardButton('Ruscha'),
        ],
        [
            KeyboardButton('Inglizcha')
        ],

    ],
    resize_keyboard=True
)

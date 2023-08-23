from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

till = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Ozbekcha'),
            KeyboardButton('Русский'),
            KeyboardButton('English')
        ]

    ],
    resize_keyboard=True
)
vacansy1 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Sherik kerak'),
            KeyboardButton('Ish joyi kerak')
        ],
        [
            KeyboardButton('Hodim kerak'),
            KeyboardButton('Ustoz kerak')
        ],
        [
            KeyboardButton('Shogird kerak')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True

)
back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('orqaga')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
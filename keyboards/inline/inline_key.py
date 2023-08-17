from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


course = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🤑Kursga yozilish", callback_data="course")
        ]
    ]
)

course_ru = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🤑Записаться на курс", callback_data="course_ru")
        ]
    ]
)
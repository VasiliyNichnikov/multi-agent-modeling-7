from aiogram.types import ReplyKeyboardMarkup

from app.view.buttons import button_start_program, \
    button_fill_in_data, button_view_completed_data

keyboard_start_actions = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
keyboard_start_actions.add(button_fill_in_data)
keyboard_start_actions.add(button_view_completed_data)
keyboard_start_actions.add(button_start_program)

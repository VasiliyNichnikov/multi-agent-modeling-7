from aiogram.types import KeyboardButton

from app.utils.config import get_config

config = get_config()
button_fill_in_data = KeyboardButton(config.keyboard_names.fill_in_data)
button_start_program = KeyboardButton(config.keyboard_names.start_program)
button_view_completed_data = KeyboardButton(config.keyboard_names.view_completed_data)

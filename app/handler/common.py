from aiogram import types
from aiogram.dispatcher import FSMContext
from app.utils.config import get_config
from app.view.keyboards import keyboard_start_actions


async def command_start(message: types.Message, state: FSMContext) -> None:
    await state.finish()
    config = get_config()
    await message.answer(config.general_messages.start_bot, reply_markup=keyboard_start_actions)

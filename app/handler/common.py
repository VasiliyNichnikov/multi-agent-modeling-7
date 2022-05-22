from aiogram import types
from aiogram.dispatcher import FSMContext

from app.handler.usercontroller import UserController
from app.models import UserModel
from app.utils.config import get_config
from app.view.keyboards import keyboard_start_actions


async def command_start(message: types.Message, state: FSMContext) -> None:
    await state.finish()
    controller = UserController()
    if controller.get_from_database(message.from_user.id) is None:
        new_user = UserModel(user_id=message.from_user.id)
        controller.add_to_database(new_user)
    config = get_config()
    await message.answer(config.general_messages.start_bot, reply_markup=keyboard_start_actions)

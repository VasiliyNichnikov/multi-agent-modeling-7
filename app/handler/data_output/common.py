from aiogram import types
from aiogram.dispatcher import FSMContext
from app.view.keyboards import keyboard_start_actions
from app.handler.data_writer.datawritercontoller import DataWriterController
from app.utils.config import get_config


async def command_data_output(message: types.Message, state: FSMContext) -> None:
    await state.finish()
    config = get_config()
    data_writer = DataWriterController().get_from_database(message.from_user.id)
    text = config.data_output_messages.output.format(data_writer.people_in_population,
                                                     data_writer.percentage_of_consumers,
                                                     data_writer.product_storage_time_in_days)
    await message.answer(text, reply_markup=keyboard_start_actions)
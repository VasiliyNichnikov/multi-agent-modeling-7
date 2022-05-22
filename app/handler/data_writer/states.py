from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from app.models.datawriter import DataWriterModel
from app.handler.data_writer.datawritercontoller import DataWriterController
from app.utils.config import get_config
from app.utils.number_handler import is_integer
from app.view.keyboards import keyboard_start_actions


class DataWriterState(StatesGroup):
    number_people_in_population = State()
    percentage_of_consumers_per_day = State()
    product_storage_time_in_days = State()


config = get_config()


async def start_data_writer(message: types.Message) -> None:
    global config
    await message.answer(config.data_writer_messages.number_people_in_population)
    await DataWriterState.number_people_in_population.set()


async def select_number_people_in_population(message: types.Message, state: FSMContext) -> None:
    global config
    await DataWriterState.next()
    is_number = await check_message(message)
    if is_number is False:
        return
    await state.update_data(people_in_population=message.text)
    await message.answer(config.data_writer_messages.percentage_of_consumers_per_day)


async def select_percentage_of_consumers_per_day(message: types.Message, state: FSMContext) -> None:
    global config
    is_number = await check_message(message)
    if is_number is False:
        return
    await state.update_data(percentage_of_consumers_per_day=message.text)
    await message.answer(config.data_writer_messages.product_storage_time_in_days)
    await DataWriterState.next()


async def select_product_storage_time_in_days(message: types.Message, state: FSMContext) -> None:
    global config
    is_number = await check_message(message)
    if is_number is False:
        return
    await state.update_data(product_storage_time_in_days=message.text)
    data = await state.get_data()

    controller = DataWriterController()
    data_writer = DataWriterModel(
        user_id=message.from_user.id,
        people_in_population=data["people_in_population"],
        percentage_of_consumers=data["percentage_of_consumers_per_day"],
        product_storage_time_in_days=data["product_storage_time_in_days"]
    )
    if controller.get_from_database(message.from_user.id) is None:
        controller.add_to_database(data_writer)
    else:
        controller.update_database(user_id=message.from_user.id, data=data)
    await message.answer(config.general_messages.task_completed, reply_markup=keyboard_start_actions)
    await state.finish()


async def check_message(message: types.Message) -> bool:
    value = message.text
    if is_integer(value) is False:
        await message.answer(config.error_messages.invalid_value)
        return False
    return True

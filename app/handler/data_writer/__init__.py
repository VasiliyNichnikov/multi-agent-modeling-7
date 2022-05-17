from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text

from app.handler.data_writer.states import start_data_writer, \
    select_number_people_in_population, \
    select_product_storage_time_in_days, \
    select_percentage_of_consumers_per_day, DataWriterState
from app.utils.config import get_config


def register(dp: Dispatcher) -> None:
    config = get_config()
    dp.register_message_handler(start_data_writer, commands="datawriter", state="*")
    dp.register_message_handler(start_data_writer, Text(equals=config.keyboard_names.fill_in_data, ignore_case=True),
                                state="*")

    dp.register_message_handler(select_number_people_in_population,
                                state=DataWriterState.number_people_in_population)
    dp.register_message_handler(select_percentage_of_consumers_per_day,
                                state=DataWriterState.percentage_of_consumers_per_day)
    dp.register_message_handler(select_product_storage_time_in_days,
                                state=DataWriterState.product_storage_time_in_days)

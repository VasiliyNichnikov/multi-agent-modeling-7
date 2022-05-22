from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text

from app.utils.config import get_config
from app.handler.data_output.common import command_data_output


def register(dp: Dispatcher) -> None:
    config = get_config()
    dp.register_message_handler(command_data_output, commands="dataoutput", state="*")
    dp.register_message_handler(command_data_output,
                                Text(equals=config.keyboard_names.view_completed_data, ignore_case=True),
                                state="*")

from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand

from app.handler.common import command_start
from app.handler.data_output.common import command_data_output
from app.utils.config import get_config
from app.utils.paths import get_token


def register_handlers_common(dp: Dispatcher) -> None:
    dp.register_message_handler(command_start, commands="start", state="*")
    dp.register_message_handler(command_data_output, commands="dataoutput", state="*")


async def set_commands(bot: Bot) -> None:
    config = get_config()
    commands = [
        BotCommand(command="/datawriter", description=config.keyboard_names.fill_in_data),
        BotCommand(command="/dataoutput", description=config.keyboard_names.view_completed_data)
    ]
    await bot.set_my_commands(commands)


async def main() -> None:
    token = get_token()
    bot = Bot(token=token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Initialize commands
    import app.handler.data_writer as data_writer
    import app.handler.data_output as data_output
    data_writer.register(dp)
    data_output.register(dp)
    register_handlers_common(dp)

    print("Start bot")
    await set_commands(bot)
    await dp.start_polling()

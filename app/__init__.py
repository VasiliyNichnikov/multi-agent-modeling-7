from aiogram import Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import Dispatcher
from aiogram.types import BotCommand

from app.handler.common import command_start
from app.utils.config import get_config
from app.utils.paths import get_token


def register_handlers_common(dp: Dispatcher) -> None:
    dp.register_message_handler(command_start, commands="start", state="*")


async def set_commands(bot: Bot) -> None:
    config = get_config()
    commands = [
        BotCommand(command="/datawriter", description=config.keyboard_names.fill_in_data)
    ]
    await bot.set_my_commands(commands)


async def main() -> None:
    token = get_token()
    bot = Bot(token=token)
    dp = Dispatcher(bot, storage=MemoryStorage())

    # Initialize commands
    import app.handler.data_writer as data_writer
    data_writer.register(dp)
    register_handlers_common(dp)

    print("Start bot")
    await set_commands(bot)
    await dp.start_polling()

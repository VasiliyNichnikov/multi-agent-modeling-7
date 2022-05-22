from abc import ABC
from typing import Dict

import toml

from app.utils.paths import get_config_path


class ElementBase(ABC):
    def __init__(self, data) -> None:
        self._data = data


class GeneralMessages(ElementBase):
    def __init__(self, data: Dict) -> None:
        super().__init__(data)
        self.__start_bot = self._data["start_bot"]
        self.__task_completer = self._data["task_completed"]

    @property
    def start_bot(self) -> str:
        return self.__start_bot

    @property
    def task_completed(self) -> str:
        return self.__task_completer


class DataWriterMessages(ElementBase):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.__number_people_in_population = self._data["number_people_in_population"]
        self.__percentage_of_consumers_per_day = self._data["percentage_of_consumers_per_day"]
        self.__product_storage_time_in_days = self._data["product_storage_time_in_days"]

    @property
    def number_people_in_population(self) -> str:
        return self.__number_people_in_population

    @property
    def percentage_of_consumers_per_day(self) -> str:
        return self.__percentage_of_consumers_per_day

    @property
    def product_storage_time_in_days(self) -> str:
        return self.__product_storage_time_in_days


class ErrorMessages(ElementBase):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.__command_not_found = data["command_not_found"]
        self.__invalid_value = data["invalid_value"]

    @property
    def command_not_found(self) -> str:
        return self.__command_not_found

    @property
    def invalid_value(self) -> str:
        return self.__invalid_value


class KeyboardNames(ElementBase):
    def __init__(self, data: Dict) -> None:
        super().__init__(data)
        self.__fill_in_data = self._data["fill_in_data"]
        self.__start_program = self._data["start_program"]
        self.__view_completed_data = self._data["view_completed_data"]

    @property
    def fill_in_data(self) -> str:
        return self.__fill_in_data

    @property
    def start_program(self) -> str:
        return self.__start_program

    @property
    def view_completed_data(self) -> str:
        return self.__view_completed_data


class DataOutputMessages(ElementBase):
    def __init__(self, data) -> None:
        super().__init__(data)
        self.__output = self._data["correct_output"]
        self.__no_data_available = self._data["no_data_available"]

    @property
    def output(self) -> str:
        return self.__output

    @property
    def no_data_available(self) -> str:
        return self.__no_data_available


class Config:
    def __init__(self, data: Dict) -> None:
        self.__keyboard_names = KeyboardNames(data["keyboard"]["names"])
        self.__general_messages = GeneralMessages(data["commands"]["general"]["messages"])
        self.__data_writer_messages = DataWriterMessages(data["commands"]["datawriter"]["messages"])
        self.__error_messages = ErrorMessages(data["commands"]["error"]["messages"])
        self.__data_output_messages = DataOutputMessages(data["commands"]["dataoutput"]["messages"])

    @property
    def keyboard_names(self) -> KeyboardNames:
        return self.__keyboard_names

    @property
    def general_messages(self) -> GeneralMessages:
        return self.__general_messages

    @property
    def data_writer_messages(self) -> DataWriterMessages:
        return self.__data_writer_messages

    @property
    def error_messages(self) -> ErrorMessages:
        return self.__error_messages

    @property
    def data_output_messages(self) -> DataOutputMessages:
        return self.__data_output_messages


__factory = None


def get_config() -> Config:
    global __factory
    if __factory is None:
        path_config = get_config_path()
        with open(path_config, 'r', encoding="utf-8") as file:
            data = toml.loads(file.read())
            __factory = Config(data)
    return __factory

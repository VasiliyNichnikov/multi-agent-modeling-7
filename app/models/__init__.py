from abc import ABC
from typing import Any


class BaseModel(ABC):
    def __init__(self, parameter: Any) -> None:
        self.__parameter: Any = parameter

    @property
    def parameter(self) -> int:
        return self.__parameter

    @parameter.setter
    def parameter(self, value) -> None:
        if value > 0:
            self.__parameter = value


class NumberPeopleInPopulation(BaseModel):
    def __init__(self, parameter: Any) -> None:
        super().__init__(parameter)


class PercentageOfConsumersPerDay(BaseModel):
    def __init__(self, parameter: Any) -> None:
        super().__init__(parameter)


class ProductStorageTimeInDays(BaseModel):
    def __init__(self, parameter: Any) -> None:
        super().__init__(parameter)

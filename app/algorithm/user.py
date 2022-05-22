from app.algorithm.states import UserStates


class User:
    def __init__(self) -> None:
        self.__state = UserStates.default
        self.__product_storage = 0

    @property
    def state(self) -> UserStates:
        return self.__state

    @property
    def product_storage(self) -> int:
        return self.__product_storage

    def change_state_to_bought(self, product_storage: int) -> None:
        self.__state = UserStates.bought
        self.__product_storage = product_storage

    def change_state_to_default(self) -> None:
        self.__state = UserStates.default
        self.__product_storage = 0

    def end_day(self) -> None:
        if self.__state == UserStates.bought:
            self.__product_storage -= 1
        else:
            raise Exception("The user does not have a product")

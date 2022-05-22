from typing import Tuple, List

from app.algorithm.states import UserStates
from app.algorithm.user import User
from app.algorithm.utils import get_only_default_users, is_user_buy_product, advertise_product_to_neighbor


class Algorithm:
    def __init__(self, number_of_cells_per_side: int,
                 product_storage: int,
                 number_of_iterations: int,
                 percentage_of_consumers: int,
                 percentage_of_advertising: int) -> None:

        self.__number_of_cells_per_side = number_of_cells_per_side
        self.__percentage_of_consumers = percentage_of_consumers
        self.__product_storage = product_storage
        self.__number_of_iterations = number_of_iterations
        self.__percentage_of_advertising = percentage_of_advertising

        # Initialize population
        self.__population = [[User() for x in range(number_of_cells_per_side)]
                             for y in range(number_of_cells_per_side)]

        self.__buyers, self.__potential_buyers = 0, number_of_cells_per_side ** 2

    def run(self) -> None:
        for day in range(self.__number_of_iterations):
            self.__one_day()

    def number_users_and_day(self) -> (int, int, int):
        for day in range(self.__number_of_iterations):
            yield self.__buyers, self.__potential_buyers, day
            self.__one_day()

    def __one_day(self) -> None:
        for y in range(self.__number_of_cells_per_side):
            for x in range(self.__number_of_cells_per_side):
                selected_user = self.__population[x][y]
                self.__check_user(selected_user, position=(x, y))

    def __check_user(self, selected_user: User, position: Tuple[int, int]) -> None:
        if selected_user.state == UserStates.default and is_user_buy_product(self.__percentage_of_consumers):
            selected_user.change_state_to_bought(self.__product_storage)
            self.__change_number_of_buyers_and_potential_buyers(add_buyer=True)
            x, y = position
            users = self.__get_default_users_nearby(x, y)
            neighbor = advertise_product_to_neighbor(users, self.__percentage_of_advertising)
            if neighbor is not None:
                self.__change_number_of_buyers_and_potential_buyers(add_buyer=True)
                neighbor.change_state_to_bought(self.__product_storage)
        elif selected_user.state == UserStates.bought:
            selected_user.end_day()
            if selected_user.product_storage <= 0:
                selected_user.change_state_to_default()
                self.__change_number_of_buyers_and_potential_buyers()
        # print(f"Buyers: {self.__buyers}; potential buyers: {self.__potential_buyers}")

    def __get_default_users_nearby(self, x: int, y: int) -> tuple[User]:
        max_cells = self.__number_of_cells_per_side

        up = self.__population[x][y + 1] if y + 1 < max_cells else None
        down = self.__population[x][y - 1] if y - 1 >= 0 else None

        right_up = self.__population[x + 1][y + 1] if x + 1 < max_cells and y + 1 < max_cells else None
        right = self.__population[x + 1][y] if x + 1 < max_cells else None
        right_down = self.__population[x + 1][y - 1] if x + 1 < max_cells and y - 1 >= 0 else None

        left_up = self.__population[x - 1][y + 1] if x - 1 >= 0 and y + 1 < max_cells else None
        left = self.__population[x - 1][y] if x - 1 >= 0 else None
        left_down = self.__population[x - 1][y - 1] if x - 1 >= 0 and y - 1 >= 0 else None

        searched_users = (up, down, right_up, right, right_down, left_up, left, left_down)
        return get_only_default_users(searched_users)

    def __change_number_of_buyers_and_potential_buyers(self, add_buyer=False) -> None:
        if add_buyer:
            self.__buyers += 1
            self.__potential_buyers -= 1
        else:
            self.__buyers -= 1
            self.__potential_buyers += 1





import random
from typing import Tuple, List

from app.algorithm.states import UserStates
from app.algorithm.user import User


def __clear_from_none_and_find_default_users(user: User | None) -> None | User:
    if user is None:
        return None
    else:
        return user if user.state == UserStates.default else None


def get_only_default_users(users: Tuple) -> tuple[User]:
    return tuple(filter(__clear_from_none_and_find_default_users, users))


def is_user_buy_product(percentage_of_consumers: int) -> bool:
    value = random.randint(0, 100)
    return value <= percentage_of_consumers


def advertise_product_to_neighbor(neighbors: Tuple[User], percentage_of_advertising: int) -> User | None:
    for neighbor in neighbors:
        if is_user_buy_product(percentage_of_advertising):
            return neighbor
    return None

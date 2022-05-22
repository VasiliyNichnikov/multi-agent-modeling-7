from app.models import UserModel
from app.database.session import SessionLocal


class UserController:
    def __init__(self) -> None:
        with SessionLocal() as session:
            self.__session = session

    def add_to_database(self, user: UserModel) -> None:
        self.__session.add(user)
        self.__session.commit()

    def get_from_database(self, user_id) -> UserModel | None:
        user = self.__session.query(UserModel).filter(UserModel.user_id == user_id).first()
        return user

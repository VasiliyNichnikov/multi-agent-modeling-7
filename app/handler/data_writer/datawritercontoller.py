from typing import Dict

from app.database.session import SessionLocal
from app.models import DataWriterModel


class DataWriterController:
    def __init__(self) -> None:
        with SessionLocal() as session:
            self.__session = session

    def add_to_database(self, data_writer: DataWriterModel) -> None:
        self.__session.add(data_writer)
        self.__session.commit()

    def get_from_database(self, user_id: int) -> DataWriterModel | None:
        data_writer = self.__session.query(DataWriterModel).filter(DataWriterModel.user_id == user_id).first()
        return data_writer

    def update_database(self, user_id, data: Dict) -> None:
        people_in_population = data["people_in_population"],
        percentage_of_consumers = data["percentage_of_consumers_per_day"],
        product_storage_time_in_days = data["product_storage_time_in_days"]

        data_writer = self.get_from_database(user_id)
        if data_writer is None:
            raise Exception("Data writer is not found")

        data_writer.people_in_population = people_in_population
        data_writer.percentage_of_consumers = percentage_of_consumers
        data_writer.product_storage_time_in_days = product_storage_time_in_days
        self.__session.commit()

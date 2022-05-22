from sqlalchemy import Integer, Column, ForeignKey

from app.database.base import Base


class DataWriterModel(Base):
    __tablename__ = "datawriters"

    user_id = Column(Integer, ForeignKey("users.user_id"))
    people_in_population = Column(Integer, nullable=False, default=0)
    percentage_of_consumers = Column(Integer, nullable=False, default=0)
    product_storage_time_in_days = Column(Integer, nullable=False, default=0)
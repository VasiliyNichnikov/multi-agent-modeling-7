from sqlalchemy import Integer, Column, UniqueConstraint, Table
from sqlalchemy.orm import relationship

from app.database.base import Base


class UserModel(Base):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("user_id"),)

    user_id = Column(Integer, nullable=False)
    data_writer = relationship("DataWriterModel", uselist=False)
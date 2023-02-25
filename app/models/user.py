from sqlalchemy import Column, String, Integer, Float, DateTime
from database.database import Base, engine
from datetime import datetime


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    nick_name = Column(String, nullable=True)
    password = Column(Integer, nullable=True)
    created_at = Column(DateTime, nullable=True, default=datetime.now())
    updated_at = Column(DateTime, nullable=True, default=datetime.now())

    def __str__(self) -> str:
        return f'id: {self.id}, name: {self.nick_name}, password: {self.password}, create: {self.created_at}'
Base.metadata.create_all(engine)
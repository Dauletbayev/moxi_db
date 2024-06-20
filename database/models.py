from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, unique=True)
    username = Column(String)
    score = Column(Integer, default=0)
    address_ton = Column(String, unique=True, nullable=True)
    reg_day = Column(DateTime)

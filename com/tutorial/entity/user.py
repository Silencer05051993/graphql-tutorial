from sqlalchemy import Column, Integer, String

from com.tutorial.entity.base import Base


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column('name', String(250))
    email = Column('email', String(250))
    password = Column('password', String(20))

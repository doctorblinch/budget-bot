import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, ForeignKey, Table, DateTime, create_engine, Float
from datetime import datetime


engine = create_engine(os.environ.get('DB_URL')) #, echo=True)
base = declarative_base()
session = sessionmaker(bind=engine)()


class User(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_payment = Column(DateTime)


class Category(base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class Payment(base):
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.now())
    amount = Column(Float)
    curency = Column(String, default='UAH')
    goal = Column(String)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User")

    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Category")


base.metadata.create_all(engine)

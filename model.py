from datetime import datetime

from sqlalchemy import create_engine, Column, Integer, String, Date, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///DBase.db')  # Создает движок базы данных БД в корневой папке проекта
Session = sessionmaker(bind=engine)  # Настраивает сессию, которая будет использоваться для взаимодействия с БД
session = Session()

Base = declarative_base()


class Users(Base):  # Определение структуры таблицы БД 'user'
    __tablename__ = 'users'

    message_id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    is_bot = Column(Integer)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    language_code = Column(String)
    is_premium = Column(Integer)
    text = Column(String)
    date = Column(DateTime, default=datetime.utcnow)


Base.metadata.create_all(engine)  # Создает все таблицы, которые были определены в классах, наследующихся от "Base"

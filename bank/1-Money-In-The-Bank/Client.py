from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


Base = declarative_base()


class Client(Base):

    __tablename__ = "clients"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    balance = Column(Float, default=0)
    password = Column(String)
    message = Column(String)
    mail = Column(String)

    def __init__(self, id, username, balance, message, mail):
        Client

    def get_username(self):
        return self.__username

    def get_balance(self):
        return self.__balance

    def get_id(self):
        return self.__id

    def get_message(self):
        return self.__message

    def set_message(self, new_message):
        self.__message = new_message


engine = create_engine("sqlite:///bank.db")
Base.metadata.create_all(engine)
session = Session(bind=engine)
user = Client(username="Rosi", balance=10, message="Hello", mail="ross_zz@mail.bg")
session.add(user)
session.commit()

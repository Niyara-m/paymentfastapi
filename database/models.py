from sqlalchemy import Column, String, Boolean, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

# пользователь
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone_number = Column(Integer)
    status = Column(Boolean, default=True)
    password = Column(String, nullable=False)

    reg_date = Column(DateTime, default=datetime.now())

# Банковские карты
class BankCard(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, autoincrement=True, primary_key=True)
    card_number = Column(Integer, nullable=False, unique=True)
    card_name = Column(String, default='Карта')
    exp_date = Column(Integer)
    balance = Column(Float, default=10000)
    reg_date = Column(DateTime, default=datetime.now())
    user_id = Column(Integer, ForeignKey('users.user_id'))
    user_fk = relationship(User)


# Услуги
class Service(Base):
    __tablename__ = 'services'
    service_id =Column(Integer, autoincrement=True, primary_key=True)

    service_name = Column(String, nullable=False)
    service_balance = Column(Float, default=0)

    service_bill = Column(Integer, nullable=False)
    reg_date = Column(DateTime, default=datetime.now())


# Платежи
class Payment(Base):
    __tablename__ = 'payments'
    payment_id = Column(Integer, autoincrement=True, primary_key=True)

    service_id = Column(Integer, ForeignKey('services.service_id'))
    card_id = Column(Integer, ForeignKey('cards.card_id'))

    amount = Column(Float, default=0)
    payment_day = Column(DateTime, default=datetime.now())

    service_fk = relationship(Service)
    card_fk = relationship(BankCard)


# Переводы
class Transfer(Base):
    __tablename__ = 'transfers'
    transfer_id = Column(Integer, primary_key=True, autoincrement=True)

    from_card = Column(Integer, ForeignKey('cards.card_id'))
    to_card = Column(Integer, ForeignKey('cards.card_id'))

    amount = Column(Float, default=0)
    transfer_date = Column(DateTime, default=datetime.now())

    from_card_fk = relationship(BankCard, foreign_keys=[from_card])
    to_card_fk = relationship(BankCard, foreign_keys=[to_card])






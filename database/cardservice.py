from database.models import BankCard, Service, Payment
from database import get_db


# Добавить карту пользователя add_card_db
def add_card_db(card_number: int, card_name: str, exp_date: int, user_id: int):
    db = next(get_db())
    new_card = BankCard(card_number=card_number, card_name=card_name, exp_date=exp_date, user_id=user_id)

    db.add(new_card)
    db.commit()

    return new_card.card_id


# Вывести все карты пользователя get_card_db
def get_card_db(user_id: int):
    db = next(get_db())
    exact_user_cards = db.query(BankCard).filter_by(user_id=user_id).all()

    return exact_user_cards


# Удалить карту пользователя delete_card_db
def delete_card_db(card_id: int):
    db = next(get_db())
    client_card = db.query(BankCard).filter_by(card_id=card_id).first()

    if client_card:
        db.delete(client_card)
        db.commit()

        return True
    return False


# Оплата за услугу
def pay_for_service_db(service_id: int, card_id: int, amount: float):
    db = next(get_db())

    # Ищем счет услуги куда должны попасть деньги
    exact_service = db.query(Service).filter_by(service_id=service_id).first()

    if exact_service:
        exact_card = db.query(BankCard).filter_by(card_id=card_id).first()

        if exact_card and exact_card.balance >= amount:
            # Вычитаем сумму из баланса карты
            exact_card.balance -= amount

            # Прибавляем сумму на счет сервиса
            exact_service.service_balance += amount

            # Записываем платеж в историю
            new_payment = Payment(service_id=service_id, card_id=card_id, amount=amount)
            db.add(new_payment)

            db.commit()

            return True

    return False


# Добавить сервис
def add_service_db(service_bill: int, service_name: str):
    db = next(get_db())

    exact_service = db.query(Service).filter_by(service_bill=service_bill).first()

    if exact_service:
        return False

    new_service = Service(service_name=service_name, service_bill=service_bill)
    db.add(new_service)

    db.commit()

    return new_service.service_id


# Вывод всех сервисов
def get_all_services_db():
    db = next(get_db())

    all_services = db.query(Service).all()

    return all_services


# Вывод информации определенной услуги
def get_exact_service_info_db(service_id: int):
    db = next(get_db())

    exact_service = db.query(Service).filter_by(service_id=service_id).first()

    return exact_service


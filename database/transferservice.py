from database.models import BankCard, Payment, Transfer
from database import get_db


# перевод с карты на карту
def transfer_money_db(from_card_id: int, to_card_number: int, amount: float):
    db = next(get_db())

    card_from = db.query(BankCard).filter_by(card_id=from_card_id).first()
    card_to = db.query(BankCard).filter_by(card_number=to_card_number).first()

    if card_from and card_to:
        if card_from.balance >= amount:
            card_from.balance -= amount
            card_to.balance += amount

            new_transfer = Transfer(from_card=from_card_id, to_card=card_to.card_id, amount=amount)
            db.add(new_transfer)
            db.commit()

            # при успешном переводе
            return 1

        # При недостаточных средствах на балансе того кто отправляет
        return -1

    # если одна или две карты не найдены в базе
    return 0


# Вывести все платежи определенной карты
def get_card_transactions_db(card_id: int):
    db = next(get_db())

    # переводы с карту на карту
    exact_card_transfers = db.query(Transfer).filter(Transfer.from_card == card_id or Transfer.to_card == card_id).all()

    # Платежи за сервисы
    exact_card_payment = db.query(Payment).filter_by(card_id=card_id).all()

    return exact_card_payment + exact_card_transfers

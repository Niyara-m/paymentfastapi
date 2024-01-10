from database.models import User
from database import get_db


# регистрация пользователя register_user_db(first_name:str, last_name:str, email:str,phone_number:int)
def register_user_db(first_name: str, last_name: str, email: str, phone_number: int, password: str):
    db = next(get_db())

    # Проверка нет ли такого номера в базе
    exact_user = db.query(User).filter_by(phone_number=phone_number).first()
    if exact_user:
        return False

    new_user = User(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, password=password)

    db.add(new_user)
    db.commit()

    return new_user.user_id
   # return {'status': 201, 'message': f'пользователь {new_user.first_name} создан!'}


# Вывод информации о пользователе get_user_info_db(user_id: int)
def get_user_info_db(user_id: int):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()

    return exact_user


# Заблокировать пользователя block_user_db(user_id:int)
def block_user_db(user_id: int):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        exact_user.status = False
        db.commit()

        return True

    return False


# Разблокировать пользователя unblock_user_db(user_id: int)
def unblock_user_db(user_id: int):
    db = next(get_db())
    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        exact_user.status = True
        db.commit()

        return True
    return False

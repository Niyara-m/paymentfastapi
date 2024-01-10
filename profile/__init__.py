from fastapi import APIRouter, HTTPException

from database.userservice import register_user_db, get_user_info_db

user_router = APIRouter()


# Запрос на регистрацию
@user_router.post('/register')
async def register_user(first_name: str, last_name: str, email: str, phone_number: int, password: str):
    result = register_user_db(first_name=first_name, last_name=last_name, email=email, phone_number=phone_number, password=password)

    if result:
        return {'status': 1, 'message': str(result)}

    return {'status': 0, 'message': 'Пользователь уже зареган'}


# Запрос на получение информации о пользователе
@user_router.get('/user-info')
async def get_user_info(user_id: int):
    result = get_user_info_db(user_id=user_id)

    if result:
        return {'status': 1, 'data': result}

    raise HTTPException(status_code=404, detail='Пользователь не найден')


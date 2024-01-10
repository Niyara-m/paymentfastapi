from fastapi import APIRouter, HTTPException

from database.cardservice import add_card_db, add_service_db, get_card_db

card_router = APIRouter()


# Запрос на добавление карты пользователю
@card_router.post('/add-card')
async def add_new_card(card_number: int,card_name: str, exp_date: int, user_id: int ):
    try:
        result = add_card_db(card_number=card_number, card_name=card_name, exp_date=exp_date, user_id=user_id )

        return {'status': 1, 'message': result}
    except:
        raise HTTPException(status_code=404, detail="Карта уже добавлена")


# Запрос на добавление услуги
@card_router.post('add-service')
async def add_new_service(service_bill:int, service_name: str):

    result = add_service_db(service_bill=service_bill, service_name=service_name)

    if result:
        return {'status': 1, 'message': result}

    return {'status': 0, 'message': 'Услуга с таким счетом существует'}


@card_router.get('/get-cards')
async def get_some_cards(user_id: int):
    result = get_card_db(user_id=user_id)

    if result:
        return {'status': 1, 'cards': result}

    raise HTTPException(status_code=404, detail="Пользователь не нвйден")
from fastapi import APIRouter, Form, Request
from starlette.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse

from database.transferservice import transfer_money_db, get_card_transactions_db
from database.cardservice import get_card_db

transfer_router = APIRouter()

# Выбор папки html файлов
template = Jinja2Templates(directory='templates')
# Сообщения об успешном переводе
messages = {}




# вывод html стр для перевода денег
@transfer_router.get('/transfer', response_class=HTMLResponse)
async def transfer_page(request: Request):
    # получаем из базы все карты опред пользователя
    all_cards = get_card_db(user_id=1)
    # Получаем сообщение если есть
    message = messages.get('status')

    # Открываем html страницу
    return template.TemplateResponse(name='transfer.html', context={'request': request,
                                                                    'cards': all_cards,
                                                                    'message': message})


# Перевод с карты на карту
@transfer_router.post('/transfer')
async def transfer_money(from_card: int = Form(),
                         to_card: int = Form(),
                         amount: float = Form()):

    # Вывод функции перевода с карты на карту
    result = transfer_money_db(from_card_id=from_card,
                               to_card_number=to_card,
                               amount=amount)

    if result == -1:
        messages['status'] = 'Недостаточно средств на балансе'

    elif result == 1:
        messages['status'] = 'Средства успешно переведены'

    elif result == 0:
        messages['status'] = 'Карта не найдена'

    return RedirectResponse(url='/transfer', status_code=302)


# Вывод баланса пол-ля и истории платежей
@transfer_router.get('/balance', response_class=HTMLResponse)
async def show_balance(request: Request):
    user_cards = get_card_db(user_id=1)
    total_balance = sum([i.balance for i in user_cards])
    history = [get_card_transactions_db(i.card_id) for i in user_cards]
    return template.TemplateResponse(name='history.html', context={'request': request,
                                                                   'user_cards': user_cards,
                                                                   'total': total_balance,
                                                                   'history': history})

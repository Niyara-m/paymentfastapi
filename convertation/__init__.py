from fastapi import APIRouter, Request, Body
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

import requests

convert_router = APIRouter()

template = Jinja2Templates(directory='templates')


# ссылка на открытие html страницы
@convert_router.get('/convert', response_class=HTMLResponse)
async def converter(request: Request):
    return template.TemplateResponse('converter.html', context={'request': request})


# ссылка api для расчетов
@convert_router.post('/convert')
async def convert_amount(currency: str = Body(), amount: float = Body()):
    url = 'https://cbu.uz/ru/arkhiv-kursov-valyut/json/'
    response = requests.get(url).json()
    print(currency, amount)

    result = [i['Rate'] for i in response if i['Ccy'] == currency]

    summa = float(amount) * float(result[0])

    return {'summa': summa}
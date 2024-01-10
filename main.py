from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from convertation import convert_router
from cards import card_router
from profile import user_router
from transfers import transfer_router

from database import Base, engine

app = FastAPI()

# Cоздаем базу данных
Base.metadata.create_all(bind=engine)

template = Jinja2Templates(directory='templates')


# вывод html страницы через fastapi
@app.get('/', response_class=HTMLResponse)
async def home(request: Request):
    return template.TemplateResponse(name="index.html",
                                     context={'request': request})

# Регистрация компонентов
app.include_router(user_router, tags=['Работа с пользователями'])
app.include_router(card_router, tags=['Работа с картами и сервисами'])
app.include_router(convert_router)
app.include_router(transfer_router, tags=['Работа с переводами денег'])

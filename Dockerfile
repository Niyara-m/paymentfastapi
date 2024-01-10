# Указываем какой язык программирования :latest
FROM python:3.9

# Копируем все файлы в докер
COPY . /pay_system

# обязательнл
WORKDIR /pay_system

# Установка библиотек python ()-не видет
RUN pip install -r requirements.txt
#RUN pip install fastapi uvicorn sqlalchemy psycopg2-binary python-multipart

# Команда для запуска
#CMD ["uvicorn", "main:app", "--reload"]

# Команда для запуска - Для тех проектов где нужна ссылка (не телеграм, а джанго проект)
CMD ["uvicorn", "main:app", "--reload", "--port=90", "--host=0.0.0.0"]
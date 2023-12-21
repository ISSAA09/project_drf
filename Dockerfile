FROM python:3

WORKDIR /code

# Копируем зависимости и код приложения
COPY ./requirements.txt /code/
RUN pip install -r requirements.txt
COPY . .

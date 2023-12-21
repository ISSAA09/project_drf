# LMS-система

## Описание проекта

Проект, который включает в себя работу с курсами и уроками. Реализована возможность подписки на курс и оплаты с помощью Stripe.

## Технологии

- Python
- Env
- Django
- DRF
- PostgreSQL
- Redis
- Celery
- Docker
- Docker Compose

## Зависимости

Зависимости, необходимые для работы проекта, указаны в файле requirements.txt
Чтобы установить зависимости, используйте команду `pip install -r requirements.txt`

## Документация

Документация находится по ссылкам:
1. Swagger `swagger/`
2. Redoc `redoc/`

## Как запустить проект

Для запуска проекта необходимо выполнить следующие шаги:
1. При необходимости установите Docker и Docker Compose на компьютер с помощью инструкции https://docs.docker.com/engine/install/
2. Cклонируйте репозиторий себе на компьютер
3. Создайте файл .env и заполните его, используя образец из файла .env.sample
4. Соберите образ с помощью команды `docker-compose build`
5. Создайте БД командой `docker-compose exec db psql -U <postgres_user>`, а затем командой `CREATE DATABASE <database_name>;`
6. Запустите контейнеры с помощью команды `docker-compose up`

## Авторы

ISSAA09

## Связь с авторами

https://github.com/ISSAA09

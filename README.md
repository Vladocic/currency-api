# Currency API

Это простое приложение на базе FastAPI для управления данными о валютах. Оно позволяет пользователям:

- Просматривать валюты
- Добавлять новые валюты
- Обновлять существующие валюты
- Удалять валюты

## Возможности:
- Получение всех валют в формате JSON.
- Получение отфильтрованных валют по коду.
- Операции CRUD (создание, чтение, обновление, удаление).
- HTML представление таблицы с валютами.

## Установка:
1. Клонируйте репозиторий:
git remote add origin https://github.com/Vladocic/currency-api.git
2. Установите зависимости:
pip install -r requirements.txt
3. Запустите приложение:
uvicorn main:app –reload

## Использование:
- Эндпоинт API `/currencies` для выполнения запросов GET, POST, PATCH, DELETE.
- HTML-таблица валют доступна по адресу `/currencies_html`.

## Лицензия:
Этот проект лицензирован по лицензии MIT.
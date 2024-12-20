# “Подписочный сервис”
## Задача:
 реализовать систему получения и оплаты подписок для онлайн-кинотеатра. 
История задачи: Мы с вами живем в мире подписок: на Yandex музыку, на Кинопоиск, на VK музыку и на многое-многое другое. Мы оплачиваем разными средствами и иногда деньги сами списываются с карточки и это порой удобно. Так подумали в сервисе “Фильмы 8 института” и решили прикрутить к себе подписочный сервис. Ваша задача помочь им в этих стремлениях.

### 

```
pip install poetry 
```

Заполни .env с пустой бд  
Установка зависимостей
```
poetry update
```
Добавление БД (миграции в папке alembic)
```
poetry run alembic upgrade head
```
Запуск приложения
```
poetry run uvicorn src.main:app --reload
```

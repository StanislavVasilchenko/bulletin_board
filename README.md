# Bulletin board
Данная работа представляет собой backend-часть для сайта объявлений. Бэкенд-часть проекта предполагает реализацию следующего функционала:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

## Содержание
- [Технологии](#технологии)
- [Начало работы](#начало-работы)
- [Установка](#установка)



## Технологии
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
- [drf-yasg](https://drf-yasg.readthedocs.io/en/stable/)
- [CORS](https://pypi.org/project/django-cors-headers/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Djoser](https://djoser.readthedocs.io/en/latest/index.html)
- [Docker](https://www.docker.com/)

## Начало работы


Создание базу данных postgres:
```
CREATE DATABASE db_name
```
Создать .env фаил:
```
Пример заполнения в файле .env.sample
```

## Установка

### Установка зависимостей
Для установки зависимостей, выполните команду:
```
pip install -r requirements.txt
```

### Запуск сервера
Чтобы запустить сервер :
```
python3 skymarket/manage.py runserver
```
Загрузка фикстур (при необходимости) :
```
python3 skymarket/manage.py loadall
```
Создание пользователя (ручной режим) :
```
python3 skymarket/manage.py create_user
```
Создание супер-пользователя (ручной режим) :
```
python3 skymarket/manage.py create_superuser
```

## Запуск проекта через docker-compose

Для запуска через docker-compose выполнить команду находясь в корне проекта:
```
docker-compose up
```


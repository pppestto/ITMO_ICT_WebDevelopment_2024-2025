# Lr3 - Django REST Framework API

## Описание

Третья лабораторная работа посвящена разработке REST API с использованием Django REST Framework. Реализованы два независимых приложения с полноценными API.

## Цели работы

- Изучить архитектуру REST API
- Работать с Django REST Framework
- Реализовать сериализаторы для преобразования моделей
- Создавать CRUD операции через API
- Тестировать API с помощью Postman

## Структура проекта

Проект состоит из двух основных приложений:

```
Lr3/
├── car_owners_project/    # Приложение Warriors
│   ├── warriors_app/      # Django приложение
│   ├── manage.py
│   └── API_DOCUMENTATION.md
│
├── printing_house/        # Приложение Printing House
│   ├── core/              # Django приложение
│   └── manage.py
│
└── Postman_Collection.json
```

## Приложения

### Warriors App

REST API для управления воинами и их навыками.

Модели:
- Warrior (воин) с расами: student, developer, teamlead
- Profession (профессия)
- Skill (навык)
- SkillOfWarrior (связь воина и навыка с уровнем освоения)

[Подробное описание Warriors App](warrior_app.md)

### Printing House

REST API для управления газетами и типографией.

Модели:
- Newspaper (газета с редакторами)
- PrintingHouse (типография)
- PostOffice (почтовое отделение)
- PrintingRun (тираж газеты)
- Distribution (распределение газет почтовым отделениям)

[Подробное описание Printing House](printing_house.md)

## Технологии

- Django 4.x+
- Django REST Framework
- Python 3.x
- SQLite / PostgreSQL
- Postman (для тестирования)

## API Endpoints (обзор)

### Warriors API
- GET/POST /api/warriors/ - список/создание воинов
- GET/PUT/DELETE /api/warriors/<id>/ - работа с конкретным воином

### Printing House API
- GET/POST /api/newspapers/ - газеты
- GET/POST /api/printing-houses/ - типографии
- GET/POST /api/post-offices/ - почтовые отделения
- GET/POST /api/printing-runs/ - тиражи
- GET/POST /api/distribution/ - распределение

## Запуск

### Warriors App
```bash
cd car_owners_project
python manage.py migrate
python manage.py runserver 8000
```

### Printing House
```bash
cd printing_house
python manage.py migrate
python manage.py runserver 8001
```

## Тестирование

Используйте Postman Collection (Postman_Collection.json) для тестирования всех endpoints.

Статус: Завершено

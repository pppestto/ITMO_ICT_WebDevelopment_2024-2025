# Lr4 - Full Stack приложение

## Описание

Четвёртая лабораторная работа это полнофункциональное Full Stack приложение с разделением на фронтенд (Vue.js 3) и бэкэнд (Django REST API).

## Цели работы

- Разработать полнофункциональное веб-приложение
- Интегрировать Django REST API с Vue.js фронтенд-ом
- Работать с современными инструментами разработки
- Понять архитектуру Full Stack приложения
- Организовать взаимодействие фронтенда и бэкэнда

## Архитектура

```
Frontend (Vue.js 3)       Backend (Django)
   Vuetify 3               Warriors API (8000)
   TypeScript              Printing House (8001)
   Port 5173 (Vite)
```

## Структура проекта

```
Lr4/
├── car_owners_project/    # Django REST API
│   ├── warriors_app/      # Warriors приложение
│   └── manage.py
│
├── printing_house/        # Django REST API
│   ├── core/              # Printing House приложение
│   └── manage.py
│
├── frontend/              # Vue.js 3 приложение
│   ├── src/
│   │   ├── components/    # Vue компоненты
│   │   ├── views/         # Страницы
│   │   ├── services/      # API сервисы
│   │   ├── stores/        # Pinia хранилище
│   │   └── App.vue
│   ├── package.json
│   └── vite.config.ts
│
├── start_backend.ps1      # Скрипт запуска бэкэнда
└── start_frontend.ps1     # Скрипт запуска фронтэнда
```

## Фронтенд технологии

- Vue.js 3 (Composition API)
- TypeScript
- Vite (сборщик)
- Vuetify 3 (UI компоненты)
- Pinia (state management)
- axios (HTTP клиент)
- Vue Router (маршрутизация)

## Структура фронтенда

```
src/
├── App.vue
├── main.ts
├── components/      # Переиспользуемые компоненты
├── views/          # Страницы приложения
├── services/       # API сервисы для запросов
├── stores/         # Pinia хранилища состояния
├── types/          # TypeScript типы
├── router/         # Vue Router конфиг
└── plugins/        # Плагины Vuetify
```

## Бэкэнд приложения

### Warriors API

REST API для управления воинами (профессиями и навыками).

[Подробное описание Warriors App](warrior_app.md)

### Printing House API

REST API для управления газетами, типографиями и их распределением.

[Подробное описание Printing House](printing_house.md)

### Frontend Integration

[Подробное описание Frontend](printing_house_frontend.md)

## Запуск приложения

### Запуск бэкэнда

```bash
# Warriors API (порт 8000)
cd car_owners_project
python manage.py migrate
python manage.py runserver

# Printing House (порт 8001, в отдельном терминале)
cd printing_house
python manage.py migrate
python manage.py runserver 8001
```

### Запуск фронтенда

```bash
cd frontend
npm install
npm run dev
```

Фронтенд: http://localhost:5173

### Через PowerShell скрипты

```powershell
.\start_backend.ps1
.\start_frontend.ps1
```

## CORS настройка

Фронтенд и бэкэнд должны быть настроены для работы вместе:

```python
# settings.py
INSTALLED_APPS = [
    'corsheaders',
    'rest_framework',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
]

CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
]
```

## API Endpoints

### Warriors API (8000)
- GET/POST /api/warriors/
- GET/PUT/DELETE /api/warriors/<id>/
- GET/POST /api/professions/
- GET/POST /api/skills/

### Printing House API (8001)
- GET/POST /api/newspapers/
- GET/POST /api/printing-houses/
- GET/POST /api/printing-runs/
- GET/POST /api/distribution/

## Тестирование

Используйте Postman Collection из Postman_Collection.json для тестирования API.

Статус: Завершено

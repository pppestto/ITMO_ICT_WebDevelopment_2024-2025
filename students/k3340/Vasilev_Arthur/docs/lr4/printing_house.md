# Printing House API (Lr4)

## Описание

Printing House приложение управляет газетами, типографиями и их распределением (аналогично Lr3, теперь интегрировано с фронтенд-ом).

## Модели

### Newspaper
```python
class Newspaper(models.Model):
    title = CharField()
    publication_index = CharField(unique=True)
    editor_first_name = CharField()
    editor_last_name = CharField()
    editor_middle_name = CharField()
    price_per_copy = DecimalField()
```

### PrintingHouse
```python
class PrintingHouse(models.Model):
    name = CharField()
    address = TextField()
    is_active = BooleanField()
```

### PostOffice
```python
class PostOffice(models.Model):
    number = CharField(unique=True)
    address = TextField()
```

### PrintingRun
```python
class PrintingRun(models.Model):
    printing_house = ForeignKey(PrintingHouse)
    newspaper = ForeignKey(Newspaper)
    circulation = IntegerField()
    # Unique constraint: (printing_house, newspaper)
```

### Distribution
```python
class Distribution(models.Model):
    post_office = ForeignKey(PostOffice)
    newspaper = ForeignKey(Newspaper)
    printing_house = ForeignKey(PrintingHouse)
    quantity = IntegerField()
```

## API Endpoints (порт 8001)

### Газеты

GET /api/newspapers/ - список
POST /api/newspapers/ - создать
GET /api/newspapers/<id>/ - получить
PUT /api/newspapers/<id>/ - обновить
DELETE /api/newspapers/<id>/ - удалить

### Типографии

GET /api/printing-houses/ - список
POST /api/printing-houses/ - создать
GET /api/printing-houses/<id>/ - получить
PUT /api/printing-houses/<id>/ - обновить

### Почтовые отделения

GET /api/post-offices/ - список
POST /api/post-offices/ - создать

### Тиражи

GET /api/printing-runs/ - список
POST /api/printing-runs/ - создать
GET /api/printing-runs/<id>/ - получить

### Распределение

GET /api/distribution/ - список
POST /api/distribution/ - создать
GET /api/distribution/<id>/ - получить

## Примеры запросов

### Создать газету
```
POST http://localhost:8001/api/newspapers/

{
  "title": "Pravda",
  "publication_index": "2312-3652",
  "editor_first_name": "Ivan",
  "editor_last_name": "Petrov",
  "price_per_copy": "15.50"
}
```

### Создать типографию
```
POST http://localhost:8001/api/printing-houses/

{
  "name": "PrintCo",
  "address": "Moscow, Tverskaya 10",
  "is_active": true
}
```

### Создать тираж
```
POST http://localhost:8001/api/printing-runs/

{
  "printing_house": 1,
  "newspaper": 1,
  "circulation": 50000
}
```

### Создать распределение
```
POST http://localhost:8001/api/distribution/

{
  "post_office": 1,
  "newspaper": 1,
  "printing_house": 1,
  "quantity": 5000
}
```

## Workflow

1. Создание газеты
2. Создание типографии
3. Определение тиража для печати
4. Распределение газет по почтовым отделениям

Дополнительно: [Вернуться к обзору Lr4](index.md)

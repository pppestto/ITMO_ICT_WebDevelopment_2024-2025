# Printing House - REST API

## Описание

Printing House это REST API для сложной системы управления типографией, газетами и их распределением.

## Модели данных

### Newspaper
Модель газеты:

```python
class Newspaper(models.Model):
    title = CharField()                 # Название газеты
    publication_index = CharField()     # Индекс издания
    editor_first_name = CharField()     # Имя редактора
    editor_last_name = CharField()      # Фамилия редактора
    editor_middle_name = CharField()    # Отчество редактора
    price_per_copy = DecimalField()     # Цена за копию
```

### PrintingHouse
Модель типографии:

```python
class PrintingHouse(models.Model):
    name = CharField()                  # Название
    address = TextField()               # Адрес
    is_active = BooleanField()          # Активна ли
```

### PostOffice
Модель почтового отделения:

```python
class PostOffice(models.Model):
    number = CharField(unique=True)     # Номер отделения
    address = TextField()               # Адрес отделения
```

### PrintingRun
Тираж газеты (связь между типографией и газетой):

```python
class PrintingRun(models.Model):
    printing_house = ForeignKey(PrintingHouse)  # Типография
    newspaper = ForeignKey(Newspaper)           # Газета
    circulation = IntegerField()                # Объём тиража
    # Unique constraint: (printing_house, newspaper)
```

### Distribution
Распределение газет почтовым отделениям:

```python
class Distribution(models.Model):
    post_office = ForeignKey(PostOffice)        # Почтовое отделение
    newspaper = ForeignKey(Newspaper)           # Газета
    printing_house = ForeignKey(PrintingHouse)  # Типография
    quantity = IntegerField()                   # Количество экземпляров
```

## API Endpoints

### Газеты API

#### Список газет
```
GET /api/newspapers/
```

Ответ:
```json
{
  "count": 10,
  "results": [
    {
      "id": 1,
      "title": "Pravda",
      "publication_index": "2312-3652",
      "editor_first_name": "Ivan",
      "editor_last_name": "Petrov",
      "price_per_copy": "15.50"
    }
  ]
}
```

#### Создать газету
```
POST /api/newspapers/
{
  "title": "Izvestiya",
  "publication_index": "2312-3653",
  "editor_first_name": "Pavel",
  "editor_last_name": "Ivanov",
  "price_per_copy": "18.50"
}
```

#### Получить/обновить/удалить газету
```
GET /api/newspapers/<id>/
PUT /api/newspapers/<id>/
DELETE /api/newspapers/<id>/
```

### Типографии API

#### Список типографий
```
GET /api/printing-houses/
```

#### Создать типографию
```
POST /api/printing-houses/
{
  "name": "PrintCo Moscow",
  "address": "Moscow, Tverskaya str. 10",
  "is_active": true
}
```

### Почтовые отделения API

#### Список отделений
```
GET /api/post-offices/
```

#### Создать отделение
```
POST /api/post-offices/
{
  "number": "101000",
  "address": "Moscow, center"
}
```

### Тиражи API

#### Список тиражей
```
GET /api/printing-runs/
```

Параметры:
- printing_house - фильтр по типографии
- newspaper - фильтр по газете
- ordering=-circulation - сортировка по объёму

#### Создать тираж
```
POST /api/printing-runs/
{
  "printing_house": 1,
  "newspaper": 1,
  "circulation": 50000
}
```

Ограничение: для каждой пары (printing_house, newspaper) может быть только один тираж.

### Распределение API

#### Список распределений
```
GET /api/distribution/
```

Параметры:
- post_office - фильтр по отделению
- newspaper - фильтр по газете
- printing_house - фильтр по типографии

#### Создать распределение
```
POST /api/distribution/
{
  "post_office": 1,
  "newspaper": 1,
  "printing_house": 1,
  "quantity": 5000
}
```

## Workflow

1. Создаётся газета
2. Создаётся типография
3. Создаётся почтовое отделение
4. Определяется тираж (сколько копий печатается)
5. Распределяется газета по отделениям (какое количество куда отправить)

## Примеры (curl)

```bash
# Получить список газет
curl http://localhost:8001/api/newspapers/

# Создать газету
curl -X POST http://localhost:8001/api/newspapers/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Daily News",
    "publication_index": "2312-1111",
    "editor_first_name": "John",
    "editor_last_name": "Smith",
    "price_per_copy": "20.00"
  }'

# Получить типографии
curl http://localhost:8001/api/printing-houses/

# Создать тираж
curl -X POST http://localhost:8001/api/printing-runs/ \
  -H "Content-Type: application/json" \
  -d '{
    "printing_house": 1,
    "newspaper": 1,
    "circulation": 100000
  }'

# Создать распределение
curl -X POST http://localhost:8001/api/distribution/ \
  -H "Content-Type: application/json" \
  -d '{
    "post_office": 1,
    "newspaper": 1,
    "printing_house": 1,
    "quantity": 5000
  }'
```

## HTTP методы

| Метод | Эндпоинт | Действие |
|-------|----------|---------|
| GET | /api/newspapers/ | Список газет |
| POST | /api/newspapers/ | Создать газету |
| GET | /api/printing-houses/ | Список типографий |
| POST | /api/printing-houses/ | Создать типографию |
| POST | /api/printing-runs/ | Создать тираж |
| GET | /api/distribution/ | Список распределений |
| POST | /api/distribution/ | Создать распределение |

Дополнительно: [Вернуться к обзору Lr3](index.md)

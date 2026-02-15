# Warriors App - REST API

## Описание

Warriors App это REST API приложение для управления воинами, их профессиями и навыками.

## Модели данных

### Warrior
Модель воина:

```python
class Warrior(models.Model):
    race_types = (
        ('s', 'student'),
        ('d', 'developer'),
        ('t', 'teamlead'),
    )
    
    race = CharField(choices=race_types)    # Раса
    name = CharField()                      # Имя воина
    level = IntegerField()                  # Уровень
    profession = ForeignKey(Profession)     # Профессия
    skill = ManyToManyField(Skill, 
            through=SkillOfWarrior)         # Навыки (через связующую таблицу)
```

### Profession
Профессия воина:

```python
class Profession(models.Model):
    title = CharField()             # Название профессии
    description = TextField()       # Описание
```

### Skill
Навык:

```python
class Skill(models.Model):
    title = CharField()             # Название навыка
```

### SkillOfWarrior
Связь воина с навыком (Many-to-Many):

```python
class SkillOfWarrior(models.Model):
    skill = ForeignKey(Skill)                   # Навык
    warrior = ForeignKey(Warrior)               # Воин
    level = IntegerField()                      # Уровень освоения навыка
```

## API Endpoints

### Список воинов
```
GET /api/warriors/
```

Параметры фильтрации:
- race - по расе (s, d, t)
- level - по уровню
- name - поиск по имени

Ответ:
```json
{
  "count": 25,
  "results": [
    {
      "id": 1,
      "name": "Aragorn",
      "race": "d",
      "level": 30,
      "profession": 1
    }
  ]
}
```

### Получить одного воина
```
GET /api/warriors/<id>/
```

Ответ:
```json
{
  "id": 1,
  "name": "Aragorn",
  "race": "d",
  "level": 30,
  "profession": 1,
  "skill": [1, 2, 3]
}
```

### Создать воина
```
POST /api/warriors/
Content-Type: application/json

{
  "name": "Legolas",
  "race": "s",
  "level": 25,
  "profession": 2
}
```

### Обновить воина
```
PUT /api/warriors/<id>/
{
  "level": 31
}
```

### Удалить воина
```
DELETE /api/warriors/<id>/
```

## Профессии API

### Список профессий
```
GET /api/professions/
```

### Создать профессию
```
POST /api/professions/
{
  "title": "Ranger",
  "description": "A skilled archer and tracker"
}
```

## Навыки API

### Список навыков
```
GET /api/skills/
```

### Создать навык
```
POST /api/skills/
{
  "title": "Archery"
}
```

## Навыки воина API

### Получить навыки воина
```
GET /api/skill-of-warrior/?warrior=1
```

### Добавить навык воину
```
POST /api/skill-of-warrior/
{
  "warrior": 1,
  "skill": 1,
  "level": 5
}
```

## Примеры использования (curl)

```bash
# Получить список воинов
curl http://localhost:8000/api/warriors/

# Получить воина по расе developer
curl http://localhost:8000/api/warriors/?race=d

# Получить одного воина
curl http://localhost:8000/api/warriors/1/

# Создать воина
curl -X POST http://localhost:8000/api/warriors/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Gimli",
    "race": "t",
    "level": 28,
    "profession": 1
  }'

# Обновить уровень воина
curl -X PUT http://localhost:8000/api/warriors/1/ \
  -H "Content-Type: application/json" \
  -d '{"level": 32}'

# Удалить воина
curl -X DELETE http://localhost:8000/api/warriors/1/
```

## HTTP методы

| Метод | Эндпоинт | Действие |
|-------|----------|---------|
| GET | /api/warriors/ | Список воинов |
| POST | /api/warriors/ | Создать воина |
| GET | /api/warriors/<id>/ | Получить воина |
| PUT | /api/warriors/<id>/ | Обновить воина |
| DELETE | /api/warriors/<id>/ | Удалить воина |

## Раса воина

Доступные значения:
- 's' - student
- 'd' - developer
- 't' - teamlead

Дополнительно: [Вернуться к обзору Lr3](index.md)

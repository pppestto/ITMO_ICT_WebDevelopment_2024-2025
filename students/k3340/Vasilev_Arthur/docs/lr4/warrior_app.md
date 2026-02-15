# Warriors App (Lr4)

## Описание

Warriors приложение в Lr4 это REST API для управления воинами, профессиями и навыками.

## Модели

### Warrior
```python
class Warrior(models.Model):
    race_types = (
        ('s', 'student'),
        ('d', 'developer'),
        ('t', 'teamlead'),
    )
    
    race = CharField(choices=race_types)
    name = CharField()
    level = IntegerField()
    profession = ForeignKey(Profession)
    skill = ManyToManyField(Skill, through=SkillOfWarrior)
```

### Profession
```python
class Profession(models.Model):
    title = CharField()
    description = TextField()
```

### Skill
```python
class Skill(models.Model):
    title = CharField()
```

### SkillOfWarrior
```python
class SkillOfWarrior(models.Model):
    skill = ForeignKey(Skill)
    warrior = ForeignKey(Warrior)
    level = IntegerField()
```

## API Endpoints

### Список воинов
```
GET http://localhost:8000/api/warriors/
```

Параметры:
- race=s|d|t - фильтр по расе
- level=20 - фильтр по уровню
- name=Aragorn - поиск по имени

### Создать воина
```
POST http://localhost:8000/api/warriors/

{
  "name": "Aragorn",
  "race": "d",
  "level": 30,
  "profession": 1
}
```

### Получить одного воина
```
GET http://localhost:8000/api/warriors/1/
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

### Обновить воина
```
PUT http://localhost:8000/api/warriors/1/

{
  "level": 31
}
```

### Удалить воина
```
DELETE http://localhost:8000/api/warriors/1/
```

## Профессии

### Список профессий
```
GET http://localhost:8000/api/professions/
```

### Создать профессию
```
POST http://localhost:8000/api/professions/

{
  "title": "Ranger",
  "description": "A skilled archer"
}
```

## Навыки

### Список навыков
```
GET http://localhost:8000/api/skills/
```

### Создать навык
```
POST http://localhost:8000/api/skills/

{
  "title": "Archery"
}
```

### Навыки воина
```
GET http://localhost:8000/api/skill-of-warrior/?warrior=1

POST http://localhost:8000/api/skill-of-warrior/

{
  "warrior": 1,
  "skill": 1,
  "level": 5
}
```

## Раса воина

- 's' - student
- 'd' - developer
- 't' - teamlead

Дополнительно: [Вернуться к обзору Lr4](index.md)

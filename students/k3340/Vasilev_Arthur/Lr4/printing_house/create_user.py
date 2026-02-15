from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

# Удаляем старого arthur если есть
User.objects.filter(username='arthur').delete()

# Создаем нового пользователя
user = User.objects.create_user(username='arthur', password='bibaboba123')

# Создаем или получаем токен
token, created = Token.objects.get_or_create(user=user)

print(f"✅ Пользователь создан: arthur")
print(f"🔐 Пароль: bibaboba123")
print(f"🔑 Токен: {token.key}")

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    Создать новый пользователский аккаунт.
    
    Требует:
    - username: строка
    - password: строка
    - password_retype: строка (должна совпадать с password)
    """
    username = request.data.get('username')
    password = request.data.get('password')
    password_retype = request.data.get('password_retype')
    
    # Проверка всех полей
    if not username or not password or not password_retype:
        return Response(
            {'error': 'username, password и password_retype обязательны'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Проверка что пароли совпадают
    if password != password_retype:
        return Response(
            {'error': 'Пароли не совпадают'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Проверка что пользователь не существует
    if User.objects.filter(username=username).exists():
        return Response(
            {'error': 'Пользователь с таким username уже существует'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Создание пользователя
    try:
        user = User.objects.create_user(username=username, password=password)
        token, _ = Token.objects.get_or_create(user=user)
        
        return Response({
            'id': user.id,
            'username': user.username,
            'auth_token': token.key,
        }, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    Аутентификация пользователя и получение токена.
    
    Требует:
    - username: строка
    - password: строка
    
    Возвращает:
    - auth_token: токен для использования в заголовке Authorization: Token <token>
    - user_id: ID пользователя
    - username: имя пользователя
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'error': 'username и password обязательны'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(username=username, password=password)
    
    if not user:
        return Response(
            {'error': 'Неверные учетные данные'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'auth_token': token.key,
        'user_id': user.id,
        'username': user.username,
    })


@api_view(['POST'])
@permission_classes([AllowAny])
def get_auth_token(request):
    """
    Получить токен аутентификации для использования в API.
    
    Использование:
    1. Отправьте POST запрос с username и password
    2. Получите токен из ответа
    3. Используйте токен в заголовке: Authorization: Token <your_token>
    """
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username or not password:
        return Response(
            {'error': 'Необходимо указать username и password'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(username=username, password=password)
    
    if not user:
        return Response(
            {'error': 'Неверные учетные данные'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    token, created = Token.objects.get_or_create(user=user)
    
    return Response({
        'auth_token': token.key,
        'user_id': user.id,
        'username': user.username,
    })


from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request

from src.users.models import User, Account


class AuthService:
    @classmethod
    def authenticate(cls, request: Request, **credentials) -> User:
        user = authenticate(request, **credentials)
        if user is None:
            raise AuthenticationFailed
        login(request, user)
        return user

    @classmethod
    def logout(cls, request: Request) -> None:
        logout(request)

    @classmethod
    def register(cls, request: Request, username: str, password: str, **kwargs) -> User:
        user = User.objects.create_user(username=username, password=password)
        account = Account.objects.create(user=user)
        if user is not None:
            login(request, user)
        return user

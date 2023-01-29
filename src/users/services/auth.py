from django.contrib.auth import authenticate, login, logout
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.request import Request

from src.users.models import User


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

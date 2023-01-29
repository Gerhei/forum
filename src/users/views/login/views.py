from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.exceptions.error_serializer import ErrorResponseSerializer
from src.users.services.auth import AuthService
from src.users.views.login.serializers import LoginSerializer


class LoginView(APIView):
    @extend_schema(operation_id='login',
                   request=LoginSerializer,
                   responses={200: None,
                              401: ErrorResponseSerializer,
                              403: ErrorResponseSerializer},
                   description='Login.')
    def post(self, request: Request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = AuthService.authenticate(request, **serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

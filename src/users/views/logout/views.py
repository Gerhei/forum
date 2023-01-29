from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.exceptions.error_serializer import ErrorResponseSerializer
from src.users.services.auth import AuthService


class LogoutView(APIView):
    @extend_schema(operation_id='logout',
                   request=None,
                   responses={200: None,
                              401: ErrorResponseSerializer,
                              403: ErrorResponseSerializer},
                   description='Logout.')
    def post(self, request: Request) -> Response:
        AuthService.logout(request)
        return Response(status=status.HTTP_200_OK)

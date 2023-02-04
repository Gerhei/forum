from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.users.services.auth import AuthService
from src.users.views.registration.serializers import UserRequestBodySerializer


class CreateUserView(APIView):
    @extend_schema(operation_id='registration',
                   request=UserRequestBodySerializer,
                   responses={201: None},
                   description='Registration.')
    def post(self, request: Request) -> Response:
        serializer = UserRequestBodySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AuthService.register(request, **serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

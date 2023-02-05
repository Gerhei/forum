from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.decorators.view_decorators import custom_extend_schema, input_serializer
from src.users.services.auth import AuthService
from src.users.views.registration.serializers import UserRequestBodySerializer


class CreateUserView(APIView):
    @custom_extend_schema(operation_id='registration',
                          request=UserRequestBodySerializer,
                          responses={201: None},
                          description='Registration.')
    @input_serializer(request_serializer_cls=UserRequestBodySerializer)
    def post(self, request: Request, request_serializer: UserRequestBodySerializer) -> Response:
        AuthService.register(request, **request_serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

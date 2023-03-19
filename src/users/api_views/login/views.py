from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.decorators.view_decorators import custom_extend_schema, input_serializer
from src.users.services.auth import AuthService
from src.users.api_views.login.serializers import LoginSerializer


class LoginView(APIView):
    @custom_extend_schema(operation_id='login',
                          request=LoginSerializer,
                          responses={200: None},
                          possible_error_statuses=[401, 403],
                          description='Login.')
    @input_serializer(request_serializer_cls=LoginSerializer)
    def post(self, request: Request, request_serializer: LoginSerializer):
        user = AuthService.authenticate(request, **request_serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

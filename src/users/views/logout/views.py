from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.decorators.view_decorators import custom_extend_schema
from src.users.services.auth import AuthService


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @custom_extend_schema(operation_id='logout',
                          request=None,
                          responses={200: None},
                          possible_error_statuses=[401, 403],
                          description='Logout.')
    def post(self, request: Request) -> Response:
        AuthService.logout(request)
        return Response(status=status.HTTP_200_OK)

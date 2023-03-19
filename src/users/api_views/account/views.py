from drf_spectacular.utils import OpenApiParameter
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.decorators.view_decorators import custom_extend_schema, input_serializer
from src.common.permissions.permissions import IsOwnerOrReadOnly
from src.users.services.account import AccountService
from src.users.api_views.account.serializers import AccountSerializer, AccountRequestBodySerializer


class AccountView(APIView):
    @custom_extend_schema(operation_id='get-account',
                          parameters=[
                              OpenApiParameter(name='slug', location=OpenApiParameter.PATH, required=True, type=str)
                          ],
                          responses={200: AccountSerializer},
                          possible_error_statuses=[404],
                          description='Get account data.')
    def get(self, request: Request, slug: str) -> Response:
        account = AccountService().get_account(slug=slug)
        serializer = AccountSerializer(account)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AccountUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    @custom_extend_schema(operation_id='update-account',
                          parameters=[
                              OpenApiParameter(name='slug', location=OpenApiParameter.PATH, required=True, type=str)
                          ],
                          request=AccountRequestBodySerializer,
                          responses={200: None},
                          possible_error_statuses=[401, 403, 404],
                          description='Update account data.')
    @input_serializer(request_serializer_cls=AccountRequestBodySerializer)
    def patch(self, request: Request, request_serializer: AccountRequestBodySerializer, slug: str) -> Response:
        account = AccountService.get_account(slug=slug)
        self.check_object_permissions(request, account)
        AccountService.update_account(account, **request_serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.exceptions.error_serializer import ErrorResponseSerializer
from src.users.services.account import AccountService
from src.users.views.account.serializers import AccountSerializer, AccountRequestBodySerializer


class AccountView(APIView):
    @extend_schema(operation_id='get-account',
                   parameters=[
                       OpenApiParameter(name='slug', location=OpenApiParameter.PATH, required=True, type=str)
                   ],
                   responses={200: AccountSerializer,
                              404: ErrorResponseSerializer},
                   description='Get account data.')
    def get(self, request: Request, slug: str) -> Response:
        account = AccountService().get_account(slug=slug)
        serializer = AccountSerializer(account)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class AccountUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(operation_id='update-account',
                   request=AccountRequestBodySerializer,
                   responses={200: None,
                              401: ErrorResponseSerializer,
                              404: ErrorResponseSerializer},
                   description='Update account data.')
    def patch(self, request: Request) -> Response:
        serializer = AccountRequestBodySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        AccountService().update_account(**serializer.validated_data, user=request.user)
        return Response(status=status.HTTP_200_OK)

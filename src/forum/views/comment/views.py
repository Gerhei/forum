from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.exceptions.error_serializer import ErrorResponseSerializer
from src.forum.models.comment import COMMENT_IS_EDITABLE_SECONDS
from src.forum.services.topic import TopicService
from src.forum.views.comment.serializers import CommentRequestBodySerializer, CommentUpdateRequestBodySerializer


class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(operation_id='create-comment',
                   request=CommentRequestBodySerializer,
                   responses={201: None,
                              401: ErrorResponseSerializer,
                              404: ErrorResponseSerializer},
                   description='Create comment.')
    def post(self, request: Request) -> Response:
        serializer = CommentRequestBodySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        TopicService().create_comment(**serializer.validated_data, user=request.user)
        return Response(status=status.HTTP_201_CREATED)


class CommentUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(operation_id='update-comment',
                   request=CommentUpdateRequestBodySerializer,
                   responses={200: None,
                              401: ErrorResponseSerializer,
                              404: ErrorResponseSerializer},
                   description=f'Edit comment if you are its author and '
                               f'no more than {COMMENT_IS_EDITABLE_SECONDS} seconds have passed since it was created.')
    def patch(self, request: Request) -> Response:
        serializer = CommentUpdateRequestBodySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        TopicService().update_comment(**serializer.validated_data, user=request.user)
        return Response(status=status.HTTP_200_OK)

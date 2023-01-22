from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.forum.services.topic import TopicService
from src.forum.views.comment.serializers import CommentRequestBodySerializer, CommentUpdateRequestBodySerializer


class CommentView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request: Request) -> Response:
        serializer = CommentRequestBodySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        TopicService().create_comment(**serializer.validated_data, user=request.user)
        return Response(status=status.HTTP_201_CREATED)

    def patch(self, request: Request) -> Response:
        serializer = CommentUpdateRequestBodySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        TopicService().update_comment(**serializer.validated_data, user=request.user)
        return Response(status=status.HTTP_200_OK)

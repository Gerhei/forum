from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.forum.views.topic.serializers import TopicSerializer, TopicRequestBodySerializer
from src.forum.services.topic import TopicService


class TopicView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request: Request, slug: str) -> Response:
        topic = TopicService().get_topic(slug=slug)
        serializer = TopicSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        serializer = TopicRequestBodySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        TopicService().create_topic(**serializer.validated_data, user=request.user)
        return Response(status=status.HTTP_201_CREATED)

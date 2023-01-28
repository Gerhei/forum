from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.exceptions.error_serializer import ErrorResponseSerializer
from src.forum.views.topic.serializers import TopicDetailSerializer, TopicRequestBodySerializer
from src.forum.services.topic import TopicService


class TopicView(APIView):
    @extend_schema(operation_id='get-topic',
                   parameters=[
                       OpenApiParameter(name='slug', location=OpenApiParameter.PATH, required=True, type=str)
                   ],
                   responses={200: TopicDetailSerializer,
                              404: ErrorResponseSerializer},
                   description='Get topic data and related comments.')
    def get(self, request: Request, slug: str) -> Response:
        topic = TopicService().get_topic(slug=slug)
        serializer = TopicDetailSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TopicCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(operation_id='create-topic',
                   request=TopicRequestBodySerializer,
                   responses={201: None,
                              401: ErrorResponseSerializer,
                              404: ErrorResponseSerializer},
                   description='Create topic with first comment.')
    def post(self, request: Request) -> Response:
        serializer = TopicRequestBodySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        TopicService().create_topic(**serializer.validated_data, user=request.user)
        return Response(status=status.HTTP_201_CREATED)

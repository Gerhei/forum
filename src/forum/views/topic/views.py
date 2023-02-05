from drf_spectacular.utils import OpenApiParameter
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.decorators.view_decorators import custom_extend_schema, input_serializer
from src.forum.views.topic.serializers import TopicDetailSerializer, TopicRequestBodySerializer
from src.forum.services.topic import TopicService


class TopicView(APIView):
    @custom_extend_schema(operation_id='get-topic',
                          parameters=[
                              OpenApiParameter(name='slug', location=OpenApiParameter.PATH, required=True, type=str)
                          ],
                          responses={200: TopicDetailSerializer},
                          possible_error_statuses=[404],
                          description='Get topic data and related comments.')
    def get(self, request: Request, slug: str) -> Response:
        topic = TopicService().get_topic(slug=slug)
        serializer = TopicDetailSerializer(topic)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TopicCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @custom_extend_schema(operation_id='create-topic',
                          request=TopicRequestBodySerializer,
                          responses={201: None},
                          possible_error_statuses=[401, 404],
                          description='Create topic with first comment.')
    @input_serializer(request_serializer_cls=TopicRequestBodySerializer)
    def post(self, request: Request, request_serializer: TopicRequestBodySerializer) -> Response:
        TopicService().create_topic(**request_serializer.validated_data, user=request.user)
        return Response(status=status.HTTP_201_CREATED)

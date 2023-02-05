from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.decorators.view_decorators import custom_extend_schema, input_serializer
from src.common.permissions.permissions import IsOwnerOrReadOnly
from src.forum.models.comment import COMMENT_IS_EDITABLE_SECONDS
from src.forum.services.topic import TopicService
from src.forum.views.comment.serializers import CommentRequestBodySerializer, CommentUpdateRequestBodySerializer


class CommentCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @custom_extend_schema(operation_id='create-comment',
                          request=CommentRequestBodySerializer,
                          responses={201: None},
                          possible_error_statuses=[401, 404],
                          description='Create comment.')
    @input_serializer(request_serializer_cls=CommentRequestBodySerializer)
    def post(self, request: Request, request_serializer: CommentRequestBodySerializer) -> Response:
        TopicService().create_comment(**request_serializer.validated_data, user=request.user)
        return Response(status=status.HTTP_201_CREATED)


class CommentUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    @custom_extend_schema(operation_id='update-comment',
                          request=CommentUpdateRequestBodySerializer,
                          responses={200: None},
                          possible_error_statuses=[401, 404],
                          description=f'Edit comment if you are its author and no more than '
                                      f'{COMMENT_IS_EDITABLE_SECONDS} seconds have passed since it was created.')
    @input_serializer(request_serializer_cls=CommentUpdateRequestBodySerializer)
    def patch(self, request: Request, request_serializer: CommentUpdateRequestBodySerializer, pk: int) -> Response:
        comment = TopicService.get_comment(comment_id=pk)
        self.check_object_permissions(request, comment)
        TopicService.update_comment(comment, **request_serializer.validated_data)
        return Response(status=status.HTTP_200_OK)

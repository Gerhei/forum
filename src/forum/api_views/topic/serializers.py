from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from src.forum.api_views.comment.serializers import CommentSerializer
from src.forum.models import Topic


class TopicDetailSerializer(serializers.ModelSerializer):
    section_id = serializers.IntegerField(required=True)
    user_id = serializers.IntegerField(required=True)
    comments = CommentSerializer(many=True, required=True)

    class Meta:
        model = Topic
        exclude = ('section', 'user')


class TopicRequestBodySerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    section_id = serializers.IntegerField(required=True)
    comment = serializers.CharField(required=True)

    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=Topic.objects.all(),
                fields=['name', 'section_id']
            )
        ]


class TopicSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    slug = serializers.CharField(required=True)
    user = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=True)

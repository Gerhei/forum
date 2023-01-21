from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from src.forum.models import Topic, Comment


class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)

    class Meta:
        model = Comment
        exclude = ('topic', 'user')


class TopicSerializer(serializers.ModelSerializer):
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

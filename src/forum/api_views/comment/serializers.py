from rest_framework import serializers

from src.forum.models import Comment


class CommentRequestBodySerializer(serializers.Serializer):
    topic_id = serializers.IntegerField(required=True)
    text = serializers.CharField(required=True)


class CommentUpdateRequestBodySerializer(serializers.Serializer):
    text = serializers.CharField(required=True)


class CommentSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(required=True)

    class Meta:
        model = Comment
        exclude = ('topic', 'user')

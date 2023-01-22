from rest_framework import serializers


class CommentRequestBodySerializer(serializers.Serializer):
    topic_id = serializers.IntegerField(required=True)
    text = serializers.CharField(required=True)


class CommentUpdateRequestBodySerializer(serializers.Serializer):
    comment_id = serializers.IntegerField(required=True)
    text = serializers.CharField(required=True)

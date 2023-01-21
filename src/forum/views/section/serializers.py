from rest_framework import serializers

from src.forum.models import Section


class TopicSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    slug = serializers.CharField(required=True)
    user = serializers.CharField(required=False)
    created_at = serializers.DateTimeField(required=True)


class SectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(required=True)
    slug = serializers.CharField(required=True)


class SectionDetailSerializer(serializers.ModelSerializer):
    parent = SectionSerializer(required=False)
    children = SectionSerializer(required=False, many=True)
    topics = TopicSerializer(required=False, many=True)

    class Meta:
        model = Section
        exclude = ('order',)


class SectionListSerializer(serializers.Serializer):
    sections = SectionSerializer(required=False, many=True)


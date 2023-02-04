from rest_framework import serializers


class AccountSerializer(serializers.Serializer):
    slug = serializers.CharField(required=True)
    reputation = serializers.IntegerField(required=True)
    description = serializers.CharField(required=True)
    username = serializers.CharField(required=True)


class AccountRequestBodySerializer(serializers.Serializer):
    slug = serializers.CharField(required=True)
    description = serializers.CharField(required=True, allow_blank=True)

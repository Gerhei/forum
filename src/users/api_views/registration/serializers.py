from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from src.users.models import User


class UserRequestBodySerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True,
                                     max_length=150,
                                     validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(required=True, label="Password")
    password2 = serializers.CharField(required=True, label="Password confirmation")

    def validate(self, data):
        validate_password(data['password'])
        if data['password'] and data['password2'] and data['password'] != data['password2']:
            raise serializers.ValidationError('The two password fields didn’t match.')
        return data

    class Meta:
        model = User
        fields = ("username", "password", "password2")


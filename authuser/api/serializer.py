from rest_framework import serializers
from authuser.models import User


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "username",
            "address",
            "contact",
            "email",
            "password",
            "designation",
            "is_full_time",
        ]


class LoginCredentialSerializer:

    class Meta:
        model = User
        fields = ["email", "password"]


class LoginResponseSerializer:

    class Meta:
        model = User
        fields = ["id", "name", "designation", "contact", "address" "email"]

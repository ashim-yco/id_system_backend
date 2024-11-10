from rest_framework import serializers
from authuser.models import User


class UserDetailRegisterSerializer(serializers.ModelSerializer):
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


class UserDetailResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "username",
            "address",
            "contact",
            "email",
            "designation",
            "is_full_time",
        ]


class LoginCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


# class LoginResponseSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "name", "designation", "contact", "address", "email"]

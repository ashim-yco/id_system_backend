from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from authuser.models import User
from authuser.api import serializer
from django.contrib.auth.hashers import make_password


class RegisterUserView(GenericAPIView):
    queryset = User
    serializer_class = serializer.UserDetailSerializer

    def post(self, request):
        user_details = self.serializer_class(data=request.data)

        if user_details.is_valid():
            exist_email = User.objects.filter(
                email=user_details.validated_data["email"]
            ).exists()

            if exist_email:
                return Response(
                    {
                        "message": "The user already exists",
                        "register_status": "User registration failed",
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            else:
                user_details.save(
                    password=make_password(password=request.data.get("password")),
                )
                return Response(
                    {"message": "User registered sucessfully"}, data=user_details
                )

        else:
            return Response({"message": "Request body cannot be null"})


class LoginUserView(GenericAPIView):

    def post(self, request):
        return Response({"message": "This is a test response for login"})


class UserDetailView(GenericAPIView):
    serializer_class = serializer.UserDetailSerializer

    def get(self, request, userid):
        try:
            user_data = User.objects.get(id=userid)
            response_data = self.serializer_class(user_data)
            return Response(response_data.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(
                {"message": "The user for the provided id does not exist!"},
                status=status.HTTP_404_NOT_FOUND,
            )


class EditUserDetailView(GenericAPIView):

    serializer_class = serializer.UserDetailSerializer

    def put(self, request, userid):
        try:
            user_data = User.objects.get(id=userid)
            user_details = self.serializer_class(
                user_data, data=request.data, partial=False
            )
            if user_details.is_valid():
                user_details.save()
                return Response(
                    {"message": "User updated successfully"}, status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"message": "Invalid data", "errors": user_details.errors},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except User.DoesNotExist:
            return Response(
                {"message": "User not found"}, status=status.HTTP_404_NOT_FOUND
            )
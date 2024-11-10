from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from authuser.models import User
from authuser.api import serializer
from django.contrib.auth.hashers import make_password
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterUserView(GenericAPIView):
    serializer_class = serializer.UserDetailRegisterSerializer

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
                user_details.validated_data["password"] = make_password(
                    user_details.validated_data["password"]
                )
                user_details.save()
                return Response(
                    {
                        "message": "User registered successfully",
                    },
                    status=status.HTTP_201_CREATED,
                )

        else:
            return Response(
                {"error": user_details.errors}, status=status.HTTP_400_BAD_REQUEST
            )


class LoginUserView(GenericAPIView):
    serializer_class = serializer.LoginCredentialSerializer

    def post(self, request):
        login_data = request.data
        login_credentials = self.serializer_class(data=login_data)

        if login_credentials.is_valid():
            username = login_credentials.validated_data.get("username")
            password = login_credentials.validated_data.get("password")

            try:
                user = User.objects.get(username=username)

                if not user.check_password(password):
                    return Response(
                        {"message": "Invalid Credentials!"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                refresh = RefreshToken.for_user(user)
                return Response(
                    {"refresh": str(refresh), "access": str(refresh.access_token)},
                    status=status.HTTP_200_OK,
                )

            except User.DoesNotExist:
                return Response(
                    {"message": "User Does not Exist!"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        else:
            return Response(
                {"message": "Invalid Credentials!"}, status=status.HTTP_400_BAD_REQUEST
            )


class UserDetailView(GenericAPIView):
    serializer_class = serializer.UserDetailResponseSerializer

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


class AllUsersResponseView(GenericAPIView):
    serializer_class = serializer.UserDetailResponseSerializer

    def get(self, request):
        try:
            all_users = User.objects.all()
            all_users = self.serializer_class(all_users, many=True)

            if all_users:
                return Response(
                    {
                        "message": "All users fetched sucesfully!",
                        "data": all_users.data,
                    },
                    status=status.HTTP_200_OK,
                )
        except:
            return Response({"message": "Failed to fetch users"})


class EditUserDetailView(GenericAPIView):
    serializer_class = serializer.UserDetailResponseSerializer

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

from django.urls import path
from authuser.api.views import user_view

urlpatterns = [
    path("registeruser/", user_view.RegisterUserView.as_view(), name="RegisterUser"),
    path("loginuser/", user_view.LoginUserView.as_view(), name="LoginUser"),
    path(
        "getuserdetails/<int:userid>",
        user_view.UserDetailView.as_view(),
        name="GetUserDetails",
    ),
]

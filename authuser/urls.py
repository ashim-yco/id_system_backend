from django.urls import include, path

urlpatterns = [
    path('authuser/', include('authuser.api.urls.urls'))
]
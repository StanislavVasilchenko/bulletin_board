from django.urls import path, include
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter

# from users.views import UserRegistrationAPIView

# from djoser.views import UserViewSet
# from rest_framework.routers import SimpleRouter


# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter

app_name = 'users'

users_router = SimpleRouter()
users_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("", include(users_router.urls)),
]

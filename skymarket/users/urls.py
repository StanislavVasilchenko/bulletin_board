from django.urls import path

from users.views import UserRegistrationAPIView

# from djoser.views import UserViewSet
# from rest_framework.routers import SimpleRouter



# TODO подключите UserViewSet из Djoser.views к нашим urls.py
# TODO для этокого рекоммендуется использовать SimpleRouter

app_name = 'users'

urlpatterns = [
    path('register/', UserRegistrationAPIView.as_view(), name='registration')
]

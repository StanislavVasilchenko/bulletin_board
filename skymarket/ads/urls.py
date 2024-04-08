from django.urls import path
from rest_framework import routers

from ads import views
from ads.apps import SalesConfig

from ads.views import AdViewSet

# TODO настройка роутов для модели

app_name = SalesConfig.name

ad_router = routers.DefaultRouter()
ad_router.register('ads', views.AdViewSet, basename='ads')

urlpatterns = [
    path('ads/me/', AdViewSet.as_view({'get': 'get_me_ads'}), name='me_ads'),
]
urlpatterns += ad_router.urls

from rest_framework import routers

from ads import views
from ads.apps import SalesConfig

# TODO настройка роутов для модели

app_name = SalesConfig.name

ad_router = routers.DefaultRouter()
ad_router.register('ads', views.AdViewSet, basename='ads')


urlpatterns = [

]
urlpatterns += ad_router.urls

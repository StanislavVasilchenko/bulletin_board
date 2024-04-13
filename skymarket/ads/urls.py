from django.urls import path, include
from rest_framework import routers

from ads import views
from ads.apps import SalesConfig

from ads.views import AdViewSet

# TODO настройка роутов для модели

app_name = SalesConfig.name

ad_router = routers.DefaultRouter()
ad_router.register('ads', views.AdViewSet, basename='ads')

comment_router = routers.DefaultRouter()
comment_router.register('comments', viewset=views.CommentViewSet, basename='comments')

urlpatterns = [
    path('ads/me/', AdViewSet.as_view({'get': 'get_me_ads'}), name='me_ads'),
    path('', include(ad_router.urls)),
    path('ads/<int:ad_id>/', include(comment_router.urls)),
]
# urlpatterns += ad_router.urls

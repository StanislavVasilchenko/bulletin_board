from rest_framework import pagination, viewsets, status
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer, AdDetailSerializer
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.permissions import IsOwner, IsAdmin
from rest_framework.response import Response


class AdPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'pages'


class AdViewSet(viewsets.ModelViewSet):
    """Контроллер для объявлений"""
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination
    filter_backends = [SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        """Авторизовананный пользователь присваивается как автор к объявлению"""
        serializer.save(author=self.request.user)

    def get_permissions(self):
        """Метод для распределения прав доступа в зависимости от действия пользователя"""
        if self.action in ['update', 'partial_update', 'create', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
            self.serializer_class = AdDetailSerializer
        return [permission() for permission in self.permission_classes]

    @action(detail=False, methods=['get'])
    def get_me_ads(self, request):
        """Отдельный экшен для вывода всех созданных объявлений пользователя"""
        if request.user.is_authenticated:
            queryset = Ad.objects.filter(author=self.request.user).order_by('-id')
            serializer = AdSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response([{'message': 'Not logged in service'}], status=status.HTTP_401_UNAUTHORIZED)


class CommentViewSet(viewsets.ModelViewSet):
    """Контроллер для комментариев"""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = AdPagination

    def perform_create(self, serializer):
        """Метод для создания комментария к конкретному объявлению.
        Пользователь и идентификатор объявления заполняются автоматически"""
        ad_id = self.kwargs['ad_id']
        ad = Ad.objects.get(id=ad_id)
        comment = serializer.save(author=self.request.user, ad=ad)
        comment.save()

    def list(self, request, *args, **kwargs):
        """Метод для вывода списка комментариев к конкретному объявлению"""

        ad_pk = self.kwargs.get('ad_id')
        queryset = self.queryset.filter(ad=ad_pk)
        serializer = self.get_serializer(queryset, many=True)
        return self.get_paginated_response(self.paginate_queryset(serializer.data))

    def get_permissions(self):
        """Метод для распределения прав доступа в зависимости от действия пользователя"""
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsOwner | IsAdmin]
        elif self.action in ['create', 'retrieve']:
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return [permission() for permission in self.permission_classes]

    def get_queryset(self):
        """Метод переопределения запроса. Вобор комментариев для конкретного объявления"""
        ad_pk = self.kwargs['ad_id']
        queryset = self.queryset.filter(ad_id=ad_pk)
        return queryset

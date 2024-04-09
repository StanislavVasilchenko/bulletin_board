from rest_framework import pagination, viewsets, status
from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny

from ads.permissions import IsAdsOwner, IsAdmin
from rest_framework.response import Response


class AdPagination(pagination.PageNumberPagination):
    page_size = 4
    page_size_query_param = 'pages'


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'create', 'destroy']:
            self.permission_classes = [IsAuthenticated, IsAdsOwner | IsAdmin]
        elif self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]
            self.serializer_class = AdDetailSerializer
        return [permission() for permission in self.permission_classes]

    @action(detail=False, methods=['get'])
    def get_me_ads(self, request):
        if request.user.is_authenticated:
            queryset = Ad.objects.filter(author=self.request.user).order_by('-id')
            serializer = AdSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response([{'message': 'Not logged in'}], status=status.HTTP_401_UNAUTHORIZED)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        ad_id = self.kwargs['ad_id']
        ad = Ad.objects.get(id=ad_id)
        comment = serializer.save(author=self.request.user, ad=ad)
        comment.save()

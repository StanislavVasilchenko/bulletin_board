from rest_framework import serializers

from ads.models import Ad
from ads.models import Comment


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    ads = serializers.CharField(source='ad.title', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    ad_id = serializers.IntegerField(source='ad.id', read_only=True)
    author_image = serializers.CharField(source='author.image', read_only=True)

    class Meta:
        model = Comment
        exclude = ['ad', 'author']


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    phone = serializers.CharField(source='author.phone', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_id = serializers.IntegerField(source='author.id', read_only=True)

    class Meta:
        model = Ad
        exclude = ['author', 'id']


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    author = serializers.CharField(source='author.first_name',
                                   read_only=True)
    phone = serializers.CharField(source='author.phone', read_only=True)

    class Meta:
        model = Ad
        exclude = ['id']

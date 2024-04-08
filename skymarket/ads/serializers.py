from rest_framework import serializers

from ads.models import Ad


# TODO Сериалайзеры. Предлагаем Вам такую структуру, однако вы вправе использовать свою

class CommentSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass


class AdSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели

    class Meta:
        model = Ad
        exclude = ['author', 'id']


class AdDetailSerializer(serializers.ModelSerializer):
    # TODO сериалайзер для модели
    pass

from django.conf import settings
from django.db import models


class Ad(models.Model):
    """Модель объявдения:
    - title: заголовок
    - description: описание
    - price: цена
    - author: автор объявдения (создается автоматически)
    - created_at: дата создания (создается автоматически)
    - image: изображение (не обязательно)"""

    title = models.CharField(max_length=250, verbose_name='Title')
    description = models.TextField(verbose_name='description')
    price = models.PositiveIntegerField(verbose_name='price')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='ad_author')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='time_created')
    image = models.ImageField(upload_to='ads/image/', verbose_name='image', blank=True, null=True)

    def __str__(self):
        return f'{self.title} - {self.author}'

    class Meta:
        verbose_name = 'Ad'
        verbose_name_plural = "Ads"
        ordering = ['-created_at']


class Comment(models.Model):
    """Модель комментария к объявлению
    - text: тект комментария
    - ad: объявление к которому написан комментарий (заполняется автоматически)
    - created_at: дата создания (создается автоматически)
    - author: автор комментария (создается автоматически)"""
    text = models.TextField(verbose_name='text')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='ad')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='time_created_comment')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='comments_author')

    def __str__(self):
        return f'{self.ad} - {self.author}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']

from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField('Текст')
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    news_img = models.ImageField(upload_to='news_img/', blank=True, verbose_name='Картинка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.id)])


class Comments(models.Model):
    article = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments',)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('news_detail', args=[str(self.article.id)])
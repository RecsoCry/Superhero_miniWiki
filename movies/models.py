from django.db import models

from django.contrib.auth import get_user_model
from django.urls import reverse


class Film(models.Model):

    MOVIES = [
        (1, 'Film'),
        (2, 'Serial'),
    ]

    title = models.CharField(max_length=100, verbose_name="Название фильма")
    year = models.IntegerField(verbose_name="Год выпуска")
    rating = models.IntegerField(verbose_name="Рейтинг")
    plot = models.TextField(verbose_name="Сюжет")
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    movie = models.PositiveSmallIntegerField( ('movies'), choices=MOVIES)
    movie_img = models.ImageField(upload_to='movie_img/', blank=True, verbose_name='Картинка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('film_detail', args=[str(self.id)])



class Comment(models.Model):
    article = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='comments',)
    comment = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.comment


    def get_absolute_url(self):
        return reverse('film_detail', args=[str(self.article.id)])
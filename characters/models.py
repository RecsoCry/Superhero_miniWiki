from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Heroes(models.Model):
    real_name = models.CharField(max_length=50, verbose_name='Реальное имя')
    superhero_name = models.CharField(max_length=100, verbose_name='Супергеройское имя')
    male = models.CharField(max_length=50, verbose_name='Пол')
    powers = models.TextField(verbose_name='Способности')
    bio = models.TextField(verbose_name='Биография')
    short_info = models.TextField(verbose_name='Краткая сводка')
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    hero_img = models.ImageField(upload_to='hero_img/', blank=True, verbose_name='Картинка')

    def __str__(self):
        return self.superhero_name

    def get_absolute_url(self):
        return reverse('hero_detail', args=[str(self.id)])

class Villains(models.Model):
    real_name = models.CharField(max_length=50, verbose_name='Реальное имя')
    villiain_name = models.CharField(max_length=100, verbose_name='Злодейский псевдоним')
    male = models.CharField(max_length=50, verbose_name='Пол')
    powers = models.TextField(verbose_name='Способности')
    bio = models.TextField(verbose_name='Биография')
    short_info = models.TextField(verbose_name='Краткая сводка')
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    vl_img = models.ImageField(upload_to='vl_img/', blank=True, verbose_name='Картинка')

    def __str__(self):
        return self.villiain_name

    def get_absolute_url(self):
        return reverse('villains_detail', args=[str(self.id)])

class Side_characters(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    full_name = models.CharField(max_length=100, verbose_name='Полное имя')
    attitude = models.CharField(max_length=100, verbose_name='Отношение')
    info = models.TextField(verbose_name='Информация')
    date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    side_img = models.ImageField(upload_to='side_img/', blank=True, verbose_name='Картинка')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('side_detail', args=[str(self.id)])
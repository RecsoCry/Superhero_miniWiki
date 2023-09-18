from django.contrib.auth.models import AbstractUser
from django.db import models

class SuperHeroUser(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True)


    def __str__(self):
        return str(self.username)
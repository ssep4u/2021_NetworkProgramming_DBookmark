from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    nickname = models.CharField('별명', max_length=20)

    def __str__(self):
        return f'{self.nickname} | {self.username}'

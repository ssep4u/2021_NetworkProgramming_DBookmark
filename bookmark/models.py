from django.db import models
from django.shortcuts import resolve_url


class Bookmark(models.Model):
    name = models.CharField('Site name', max_length=30)
    url = models.URLField('Site URL')

    def __str__(self):
        return f'{self.name} | {self.url}'

    def get_absolute_url(self):
        return resolve_url('bookmark:detail', pk=self.pk)

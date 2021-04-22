from django.db import models


class Bookmark(models.Model):
    name = models.CharField('Site name', max_length=30)
    url = models.URLField('Site URL')

    def __str__(self):
        return f'{self.name} | {self.url}'

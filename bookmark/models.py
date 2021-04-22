from django.db import models


class Bookmark(models.Model):
    name = models.CharField('Site name', max_length=30)
    url = models.URLField('Site URL')

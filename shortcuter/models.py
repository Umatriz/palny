from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Link(models.Model):
    """docstring for Link."""

    sourse_link = models.URLField('Your link', max_length = 550)
    url = models.SlugField('Your slug', unique = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)

    def __str__(self):
        return self.sourse_link

    def get_absolute_url(self):
        return f'{self.sourse_link}'

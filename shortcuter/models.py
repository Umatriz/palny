from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Link(models.Model):

    sourse_link = models.URLField('link', max_length = 550)
    views = models.PositiveIntegerField('views', default = 0)
    url = models.SlugField('slug')
    author = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = True)

    class Meta:
        unique_together = ('author', 'url')

    def __str__(self):
        return self.sourse_link

    def get_absolute_url(self):
        return f'{self.sourse_link}'

    def get_user_link(self):
        return f'{self.author.id}/{self.url}'

    def get_absolute_edit(self):
        return reverse('edit', kwargs = {'pk': self.id})

    def get_absolute_delete(self):
        return reverse('delete', kwargs = {'pk': self.id})

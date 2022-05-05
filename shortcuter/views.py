from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View

from . import models


def main(request):
    return render(request, 'shortcuter/index.html')

def add_url(request):
    return render(request, 'shortcuter/add.html')

class Short(View):
    def get(self, request, slug):
        link = models.Link.objects.get(url = slug)
        return redirect(link)

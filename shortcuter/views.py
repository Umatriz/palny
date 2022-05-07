from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View

from . import models
from . import forms


def main(request):
    return render(request, 'shortcuter/index.html')

def add_url(request):
    form = forms.LinkForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, 'shortcuter/add.html', {'form': form})

class Short(View):
    def get(self, request, slug):
        link = models.Link.objects.get(url = slug)
        return redirect(link)

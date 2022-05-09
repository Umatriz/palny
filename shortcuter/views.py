from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.urls import reverse

from . import models
from . import forms


def main(request):
    return render(request, 'shortcuter/index.html')

class Short(View):
    def get(self, request, slug, pk):
        link = models.Link.objects.get(author = pk, url = slug)
        return redirect(link)

def add_url(request):
    form = forms.LinkForm(request.POST)
    if request.user.is_authenticated:
        if form.is_valid():
            form = form.save(commit = False)
            form.author = request.user
            form.save()
        return render(request, 'shortcuter/add.html', {'form': form})
    else:
        return redirect('login')

def links_list(request):
    links = models.Link.objects.filter(author = request.user)
    context = {
        'links': links,
    }
    return render(request, 'shortcuter\profile.html', context)

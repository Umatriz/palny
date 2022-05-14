from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.views.generic import UpdateView
from django.contrib.auth.models import User

from . import models
from . import forms


def main(request):
    return render(request, 'shortcuter/index.html')

def short(self, request, slug, pk):
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
    full_link = request.build_absolute_uri
    context = {
        'links': links,
        'full_link': full_link,
    }
    return render(request, 'shortcuter/profile.html', context)

def update_link(request, pk):
    if request.user.is_authenticated:
        link = models.Link.objects.filter(author = request.user, id = pk).first()
        print(link)
        form = forms.LinkForm(request.POST or None, instance = link)
        if form.is_valid():
            form = form.save(commit = False)
            form.author = request.user
            form.save()
            return redirect('profile')
        return render(request, 'shortcuter/update.html', {'form': form, 'link': link})
    else:
        return redirect('login')

def delete_link(request, pk):
    link = models.Link.objects.filter(author = request.user, id = pk).first()
    link.delete()

    return redirect('profile')

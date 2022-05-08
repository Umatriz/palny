from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from django.contrib.auth.models import User

from . import models
from . import forms


def main(request):
    return render(request, 'shortcuter/index.html')

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

class Short(View):
    def get(self, request, slug):
        link = models.Link.objects.get(url = slug)
        return redirect(link)

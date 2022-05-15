from django import forms

from . import models


class LinkForm(forms.ModelForm):
    """docstring for LinkForm."""
    class Meta:
        model = models.Link
        fields = ('sourse_link', 'url', 'author')
        widgets = {
            'author': forms.HiddenInput(),
        }

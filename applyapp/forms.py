from django import forms
from django.db.models import CharField
from django.forms import IntegerField

from applyapp.models import Apply


class ApplyForm(forms.ModelForm):
    class Meta:
        model = Apply
        fields = ('offer', 'work', 'language', 'framwork', 'answer', 'file')

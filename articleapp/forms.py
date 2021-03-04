from django.db.models import TextField
from django.forms import ModelForm
from django import forms

from articleapp.models import Article


class CreateArticleForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'height: auto;text-align: left;'}))

    class Meta:
        model = Article
        fields = ['title', 'introduce', 'content','deadline','question', 'thumbnail']# '__all__' 설정시 전체 필드 추가


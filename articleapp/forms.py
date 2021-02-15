from django.db.models import TextField
from django.forms import ModelForm

from articleapp.models import Article


class CreateArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'introduce', 'content','deadline','question', 'thumbnail']# '__all__' 설정시 전체 필드 추가


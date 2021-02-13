from django.db.models import TextField
from django.forms import IntegerField, CharField, ChoiceField, Form

from articleapp.models import Article


class CreateArticleForm(Form):
    # for Article
    title = CharField(label='프로젝트 제목')
    Introduce = CharField(label='간단한 프로젝트 소개')
    Local = ChoiceField( initial='서울특별시')
    lapse = ChoiceField(  initial='팀빌딩')
    deadline = IntegerField(label='예상 소요 기간', initial=0)
    now_pd = ChoiceField( initial='0')
    now_dev= ChoiceField( initial='0')
    now_designer= ChoiceField(initial='0')

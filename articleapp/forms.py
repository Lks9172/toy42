from django.db.models import TextField
from django.forms import IntegerField, CharField, ChoiceField, Form

from articleapp.models import Article


class CreateArticleForm(Form):
    # for Article
    title = CharField(max_length = 20, label='프로젝트 제목')
    Introduce = CharField(max_length=50, label='간단한 프로젝트 소개')
    Local = ChoiceField(choices=Article.local_choices, initial='서울특별시')
    lapse = ChoiceField( choices=Article.lapse_CHOICES, initial='팀빌딩')
    deadline = IntegerField(label='예상 소요 기간', initial=0)
    now_pd = ChoiceField(choices=Article.personnel_CHOICES, initial='0')
    now_dev= ChoiceField(choices=Article.personnel_CHOICES, initial='0')
    now_designer= ChoiceField(choices=Article.personnel_CHOICES, initial='0')

    # for TeamMember
    pd = ChoiceField(choices=Article.personnel_CHOICES, initial='0')
    dev = ChoiceField(choices=Article.personnel_CHOICES, initial='0')
    designer = ChoiceField(choices=Article.personnel_CHOICES, initial='0')

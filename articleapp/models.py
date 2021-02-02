from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, CharField, TextField, IntegerField, ManyToManyField


class Article(models.Model):
    local_choices = {
        ('02', '서울특별시'),  # 오른쪽에 있는 것이 화면에 보인다.
        ('051','부산광역시'),
        ('053','대구광역시'),
        ('042','대전광역시'),
        ('032', '인천광역시'),
        ('062','광주광역시'),
        ('052','울산광역시'),
        ('044', '세종특별자치시'),
        ('031','경기도'),
        ('033','강원도'),
        ('043', '충청북도'),
        ('041','충청남도'),
        ('063','전라북도'),
        ('061', '전라남도'),
        ('054','경상북도'),
        ('055','경상남도'),
        ('064','제주특별자치도')
    }

    lapse_CHOICES = {
        (1,'팀빌딩'),
        (2,'아이디어 구상'),
        (3,'기획완료')
    }

    role_CHOICES = {
        ('Planner', '기획자'),  # 오른쪽에 있는 것이 화면에 보인다.
        ('developer','개발자'),
        ('designer','디자이너')
    }

    personnel_CHOICES = {
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    }

    Publisher = ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    title = CharField(max_length = 20)
    Introduce = TextField(max_length = 50)
    local = CharField(max_length=3, choices=local_choices,)
    lapse = IntegerField( choices=lapse_CHOICES)
    deadline = IntegerField()

    now_pd = IntegerField(choices=personnel_CHOICES, default=0)
    now_dev= IntegerField(choices=personnel_CHOICES, default=0)
    now_designer= IntegerField(choices=personnel_CHOICES, default=0)

    def __str__(self):
        return '%s by %s' % (self.Publisher, self.title)


class TeamMember(models.Model):

    project = models.OneToOneField(Article, on_delete=models.CASCADE,  related_name='TeamMember')
    pd = IntegerField(choices=Article.personnel_CHOICES, default=0)
    dev = IntegerField(choices=Article.personnel_CHOICES, default=0)
    designer = IntegerField(choices=Article.personnel_CHOICES, default=0)

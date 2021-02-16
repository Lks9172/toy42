from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Model, ForeignKey, CharField, TextField, FileField,IntegerField

from articleapp.models import Article


class Apply(Model):
    DECISION_CHOICES = (
        (1, '결정전'),
        (2, '수락'),
        (3, '거절'),
    )

    offer = ForeignKey(Article, on_delete=models.CASCADE, related_name='offer')
    applicant = ForeignKey(User, on_delete=models.CASCADE, related_name='applicant')
    work = CharField(max_length=20)
    language = CharField(max_length=50)
    framwork = CharField(max_length=50)
    answer = TextField(max_length=100)
    file = FileField(upload_to='files/', null=True)
    decision = IntegerField(default=1, choices=DECISION_CHOICES)
    comment = TextField(max_length=200, null=True, default="확인 전 입니다.", blank=True)

    def __str__(self):
        return '%s 프로젝트에 대한 %s의 지원' % (self.offer, self.applicant)
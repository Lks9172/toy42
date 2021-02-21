from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, CharField, TextField, IntegerField, BooleanField, ImageField


class Article(models.Model):

    publisher = ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    title = CharField(max_length=20)
    introduce = CharField(max_length=50)
    content = TextField(max_length=100,  default=' ')
    deadline = IntegerField( default= 0)
    activation = BooleanField(default=True)
    question = CharField(max_length=30, default=' ')
    thumbnail = ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '[%s] 의 [%s]' % (self.publisher, self.title)

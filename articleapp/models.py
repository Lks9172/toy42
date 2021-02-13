from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey, CharField, TextField, IntegerField, BooleanField, ImageField


class Article(models.Model):

    publisher = ForeignKey(User, on_delete=models.CASCADE, related_name='article')
    title = CharField(max_length=20)
    introduce = TextField(max_length=50)
    content = CharField(max_length=100,  default=' ')
    deadline = IntegerField( default= 0)
    activation = BooleanField(default=True)
    question = CharField(max_length=30, default=' ')
    thumbnail = ImageField()

    def __str__(self):
        return '%s by %s' % (self.publisher, self.title)

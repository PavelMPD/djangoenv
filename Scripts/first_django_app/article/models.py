# coding: utf-8
import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    class Meta:
        db_table = 'article'

    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    likes = models.IntegerField(default=0)


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    date = models.DateTimeField(default=datetime.datetime.now())
    user = models.ForeignKey(User, default=1)
    text = models.TextField(verbose_name='Текст комментария')
    article = models.ForeignKey(Article)
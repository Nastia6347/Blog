# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    class Meta():
        db_table = 'article'

    article_title = models.CharField(max_length=200)
    article_text = models.TextField()
    article_data = models.DateTimeField()
    article_likes = models.IntegerField(default=0)


class Comments(models.Model):
    class Meta():
        db_table = 'comments'

    comments_data = models.DateTimeField(blank=True, null=True)
    comments_text = models.TextField(verbose_name="Текс комментария")
    comments_article = models.ForeignKey(Article)
    comments_from = models.ForeignKey(User, blank=True, null=True)
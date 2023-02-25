import datetime

from django.db import models


# Create your models here.

class Question(models.Model):
    content = models.CharField(max_length=100)

    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=10)


class Roles(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    create_time = models.DateTimeField(default=datetime.datetime.now)
    status = models.IntegerField()


class TbUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)


class TbMenus(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    icon = models.ImageField()

import datetime

from django.db import models
from django.utils import timezone


# Create your models here.

class Question(models.Model):
    content = models.CharField(max_length=100)

    pub_date = models.DateTimeField("date published")

    def is_published_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.datetime(day=1)


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
    icon = models.CharField(max_length=200)


class TbRules(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    father_id = models.IntegerField()
    rule_name = models.CharField(max_length=100)
    is_menu = models.BooleanField(default=False)

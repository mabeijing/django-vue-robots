from django.db import models


# Create your models here.

class Question(models.Model):
    content = models.CharField(max_length=100)

    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=10)
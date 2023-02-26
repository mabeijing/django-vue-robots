from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Question


# Create your views here.

def index(request):
    return HttpResponse("hello world!")


def detail(request, question_id):
    q = Question.objects.get(pk=question_id)
    return HttpResponse(f"结果是{q.content}")


def vote(request, question_id):
    q = get_object_or_404(Question, pk=question_id)
    return HttpResponse("vote is %s" % q.content)

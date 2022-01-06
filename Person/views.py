from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    return HttpResponse("Как говорил великий: Лучше ты на коне чем конь на тебе!")


# Create your views here.

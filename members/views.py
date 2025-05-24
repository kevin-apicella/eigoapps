from django.shortcuts import render
from django.http import HttpResponse


def tryitout2(request):
    return HttpResponse('Members /test page showing up correctly!!!!')
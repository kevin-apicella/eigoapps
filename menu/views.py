from django.shortcuts import render
from django.http import HttpResponse


def menu_view(request):
    request.session.flush()
    return render(request, 'menu.html')
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def home(request):
    return render(request, 'acceuil/acceuil.html')


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})
# Create your views here.

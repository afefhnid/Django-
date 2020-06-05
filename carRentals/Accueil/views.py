from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def home(request):
    agences=[
        {
            "name": "Molecule Man",
            "city": "Molecule Man",
            "prix": "45" ,
            "car": [
            "Radiation resistance",
            "Turning tiny",
            "Radiation blast"
            ]
        },
        {
            "name": "Molecule Man",
            "city": "Molecule Man",
            "prix": "52",
            "car": [
            "Radiation resistance",
            "Turning tiny",
            "Radiation blast"
            ]
        }
    ]
    locations=[
        {
            "name": "Molecule Man",
            "city": "Molecule Man",
            "prix": "45" ,
            "car": [
            "Radiation resistance",
            "Turning tiny",
            "Radiation blast"
            ]
        },
        {
            "name": "Molecule Man",
            "city": "Molecule Man",
            "prix": "52",
            "car": [
            "Radiation resistance",
            "Turning tiny",
            "Radiation blast"
            ]
        }
    ]
    return render(request, 'acceuil/acceuil2.html', {'agences':agences,'locations':locations})


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})
# Create your views here.


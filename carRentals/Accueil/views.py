from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .forms import DateForm, SnippetForm, LoginForm
from django.http import HttpResponseRedirect

from bootstrap_datepicker_plus import DateTimePickerInput
from .models import Vehicule


def home1(request):
    agences = [
        {
            "name": "Molecule Man",
            "city": "Molecule Man",
            "prix": "45",
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
    locations = [
        {
            "name": "Molecule Man",
            "city": "Molecule Man",
            "prix": "45",
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
    return render(request, 'acceuil/acceuil2.html', {'agences': agences, 'locations': locations})


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})
# Create your views here.


def home(request):
    query_results = Vehicule.objects.all().values('marque')

    print(query_results)
    if request.method == "POST":
        form = DateForm(request.POST)
        if form.is_valid():
            lieu = form.cleaned_data['lieu']
            print(lieu)
            return HttpResponseRedirect('snippet')

            # dateRetrait = form.cleaned_data['dateRetrait']
            # dateRetour = form.cleaned_data['dateRetour']

    form = DateForm()

    return render(request, 'acceuil/acceuil.html', {'form': form, 'Vehicule': query_results})


def snippet_detail(request):

    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            # dateRetrait = form.cleaned_data['dateRetrait']
            # dateRetour = form.cleaned_data['dateRetour']

    form = SnippetForm()
    return render(request, 'acceuil/acceuil.html', {'form': form})


def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()

            # dateRetrait = form.cleaned_data['dateRetrait']
            # dateRetour = form.cleaned_data['dateRetour']

    form = LoginForm()
    return render(request, 'acceuil/login.html', {'form': form})


def compare(request):
    query_results = Vehicule.objects.all().values()
    print("ee", query_results)
    return render(request, 'Vehicule/Vehicule.html', {'Vehicules': query_results})

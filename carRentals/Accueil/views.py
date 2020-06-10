from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from .forms import DateForm, SnippetForm, LoginForm
from django.http import HttpResponseRedirect

from bootstrap_datepicker_plus import DateTimePickerInput
from .models import Vehicule, Agence

from django.contrib.auth import login as dj_login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})
# Create your views here.


def home(request):

    query_results = Vehicule.objects.all().values('marque')
    locations = Vehicule.objects.all()[:6].values()
    agences = Agence.objects.all()[:6].values()
    if request.method == "POST":
        form = DateForm(request.POST)
        if form.is_valid():
            lieu = form.cleaned_data['lieu']
            print(lieu)
            return HttpResponseRedirect('snippet')

            # dateRetrait = form.cleaned_data['dateRetrait']
            # dateRetour = form.cleaned_data['dateRetour']

    form = DateForm()

    return render(request, 'acceuil/acceuil.html', {'form': form, 'Vehicule': query_results, 'agences': agences, 'locations': locations})


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
    return render(request, 'Vehicule/Vehicule.html', {'Vehicules': query_results})


def agence(request):
    query_results = Agence.objects.all().values()
    return render(request, 'Agence/Agence.html', {'Agences': query_results, 'a': "query_results"})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            dj_login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'acceuil/signup.html', {'form': form})

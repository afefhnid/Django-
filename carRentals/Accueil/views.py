from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime


def home(request):
    """ Exemple de page non valide au niveau HTML pour que l'exemple soit concis """
    return HttpResponse("""
    <h1>Votre prochaine voiture vous attend !</h1>
    <p>Louez une voiture à l'heure ou à la journée!</p>
    """)


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})
# Create your views here.

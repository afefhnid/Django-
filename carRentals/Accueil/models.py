from django.db import models
import datetime

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django import forms


class Snippet(models.Model):
    lieu = models.CharField(max_length=100)
    dateRetour = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2'
        })
    )

    def __str__(self):

        return self.lieu
    # Create your models here.


class Login(models.Model):
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):

        return self.email

    # Create your models here.


class Vehicule(models.Model):
    marque = models.CharField(max_length=100)
    nbPorte = models.IntegerField()
    modele = models.CharField(max_length=100)
    prix = models.IntegerField()
    image = models.CharField(max_length=500)

    def __str__(self):

        return self.marque

    # Create your models here.


class Agence(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    horaire = models.CharField(max_length=100)

    def __str__(self):

        return self.nom

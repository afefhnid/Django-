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

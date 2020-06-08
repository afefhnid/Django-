from django import forms
from .models import Snippet, Login
from bootstrap_datepicker_plus import DateTimePickerInput
from django.views import generic


class DateForm(forms.Form):
    lieu = forms.CharField(label="Lieu de retrait ")

  # dateRetrait = forms.DateTimeField (
    """  input_formats=['%d/%m/%Y %H:%M'],
         widget=forms.DateTimeInput(attrs={
             'class': 'form-control datetimepicker-input',
             'data-target': '#datetimepicker1'
         })
     )
     dateRetour = forms.DateTimeField(
         input_formats=['%d/%m/%Y %H:%M'],
         widget=forms.DateTimeInput(attrs={
             'class': 'form-control datetimepicker-input',
             'data-target': '#datetimepicker2'
         })
     ) """


class SnippetForm(forms.ModelForm):

    class Meta:
        model = Snippet
        fields = ('lieu', )


class LoginForm(forms.ModelForm):

    class Meta:
        model = Login
        fields = ('email', 'password')

from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.home),
    path('snippet', views.snippet_detail),
    path('login', views.login),
    path('date', views.date_actuelle),
    path('Vehicule', views.compare),
    path('Agences', views.agence),
    url(r'signup', views.signup, name='signup'),
]

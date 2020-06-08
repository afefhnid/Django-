from django.urls import path
from . import views

urlpatterns = [
    path(' ', views.home),
    path('snippet', views.snippet_detail),
    path('login', views.login),
    path('date', views.date_actuelle),

]

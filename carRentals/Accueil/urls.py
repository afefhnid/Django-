from django.urls import path
from . import views

urlpatterns = [
    path('', views.home1),
    path('snippet', views.snippet_detail),
    path('login', views.login),
    path('date', views.date_actuelle),

]

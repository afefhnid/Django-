from django.urls import path
from . import views

urlpatterns = [
<<<<<<< HEAD
    path('', views.home1),
=======
    path('', views.home),
>>>>>>> b8641e6b3134557c5db494ce73889cd26224c44e
    path('snippet', views.snippet_detail),
    path('login', views.login),
    path('date', views.date_actuelle),
    path('Vehicule', views.compare),
]

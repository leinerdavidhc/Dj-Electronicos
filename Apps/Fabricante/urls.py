from django.urls import path
from Apps.Fabricante.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
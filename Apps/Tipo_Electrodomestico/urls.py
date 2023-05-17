from django.urls import path
from Apps.Tipo_Electrodomestico.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
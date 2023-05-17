from django.urls import path
from Apps.Componente_Piezas.views import home

urlpatterns = [
    path('inicio/', home, name= 'home'),
]
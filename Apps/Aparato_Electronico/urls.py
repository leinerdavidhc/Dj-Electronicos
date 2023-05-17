from django.urls import path
from Apps.Aparato_Electronico.views import home

urlpatterns = [
    path('', home, name= 'home'),
]
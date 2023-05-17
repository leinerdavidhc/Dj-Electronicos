from django.urls import path
from Apps.Proveedor.views import home

urlpatterns = [
    path('', home, name= 'home'),
]
from django.contrib import admin
from django.urls import path
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('AparatoElectronico/', include('Apps.Aparato_Electronico.urls')),
    path('ComponentePiezas/', include('Apps.Componente_Piezas.urls')),
    path('Fabricante/', include('Apps.Fabricante.urls')),
    path('TipoElectrodomestico/', include('Apps.Tipo_Electrodomestico.urls')),
]
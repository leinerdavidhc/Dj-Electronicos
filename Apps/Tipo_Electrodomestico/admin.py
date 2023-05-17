from django.contrib import admin
from Apps.Tipo_Electrodomestico.models import TipoElectrodomestico

# Register your models here.

class TipoElectrodomesticoAdmin(admin.ModelAdmin):
    pass


admin.site.register(TipoElectrodomestico, TipoElectrodomesticoAdmin)
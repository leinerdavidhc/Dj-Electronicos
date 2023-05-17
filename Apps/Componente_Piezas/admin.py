from django.contrib import admin
from Apps.Componente_Piezas.models import Componente

# Register your models here.

class ComponenteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Componente, ComponenteAdmin)
from django.contrib import admin
from Apps.Fabricante.models import Fabricante

# Register your models here.

class FabricanteEAdmin(admin.ModelAdmin):
    pass


admin.site.register(Fabricante, FabricanteEAdmin)
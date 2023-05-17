from django.contrib import admin
from Apps.Proveedor.models import Proveedores

# Register your models here.

class ProveedoresAdmin(admin.ModelAdmin):
    pass


admin.site.register(Proveedores, ProveedoresAdmin)
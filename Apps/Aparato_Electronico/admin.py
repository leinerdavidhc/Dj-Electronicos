from django.contrib import admin
from Apps.Aparato_Electronico.models import AparatoE

# Register your models here.

class AparatoEAdmin(admin.ModelAdmin):
    pass


admin.site.register(AparatoE, AparatoEAdmin)
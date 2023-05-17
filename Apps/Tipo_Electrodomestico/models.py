from django.db import models
from Apps.Aparato_Electronico.models import AparatoE

class TipoElectrodomestico(models.Model):
    aparatoE = models.ForeignKey(AparatoE, on_delete=models.CASCADE)
    caracteristicas = models.CharField(help_text= "Ingrese las caracteristicas", max_length=100)
    nombre = models.CharField(help_text= "Ingrese nombre", max_length=36)

    def _str_(self):
        return self.nombre

    class Meta:
        verbose_name = "Tipo Electrodomestico"
        verbose_name_plural = "Tipo Electrodomestico"
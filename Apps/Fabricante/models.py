from django.db import models
from Apps.Componente_Piezas.models import Componente

class Fabricante(models.Model):
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    nameFabricante = models.CharField(help_text= "Ingrese nombre del fabricante", max_length=100)
    domicilio = models.CharField(help_text= "Ingrese domicilio social", max_length=36)

    def _str_(self):
        return self.domicilio

    class Meta:
        verbose_name = "Fabricante"
        verbose_name_plural = "Fabricantes"
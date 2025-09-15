from django.db import models
from .Almacen import Almacen

class Estante(models.Model):
    nro_estante = models.PositiveIntegerField()
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Estante"
        verbose_name_plural = "Estantes"

    def __str__(self):
        return f"Estante {self.nro_estante} en {self.almacen}"

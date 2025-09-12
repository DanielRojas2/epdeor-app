from django.db import models
from .Partida import Partida
from .UdM import UdM

class Material(models.Model):
    material = models.CharField(max_length=100, unique=True)
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    unidad_medida = models.ForeignKey(UdM, on_delete=models.CASCADE)
    nivel_minimo = models.PositiveIntegerField()
    cantidad_existente = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"

    def __str__(self):
        return f"{self.material} - {self.partida.codigo} - {self.unidad_medida.unidad_medida}"

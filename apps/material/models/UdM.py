from django.db import models

class UdM(models.Model):
    unidad_medida = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = "Unidad de Medida"
        verbose_name_plural = "Unidades de Medida"

    def __str__(self):
        return self.unidad_medida

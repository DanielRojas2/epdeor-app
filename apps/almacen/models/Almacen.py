from django.db import models

class Almacen(models.Model):
    ALMACEN_CHOICES = (
        ('material', 'Material'),
        ('archivos', 'Archivos'),
    )
    tipo_almacen = models.CharField(max_length=8, choices=ALMACEN_CHOICES)
    ubicacion = models.TextField()
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Almacén"
        verbose_name_plural = "Almacenes"

    def __str__(self):
        return f"{self.tipo_almacen} - {self.ubicacion}"

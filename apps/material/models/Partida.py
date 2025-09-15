from django.db import models

class Partida(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    denominacion = models.CharField(max_length=35, unique=True)
    descripcion = models.TextField()

    class Meta:
        verbose_name = "Partida"
        verbose_name_plural = "Partidas"

    def __str__(self):
        return f"{self.codigo} - {self.descripcion}"

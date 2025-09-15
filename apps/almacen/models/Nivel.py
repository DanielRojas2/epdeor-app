from django.db import models

class Nivel(models.Model):
    nro_nivel = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Nivel"
        verbose_name_plural = "Niveles"

    def __str__(self):
        return f"Nivel {self.nro_nivel}"

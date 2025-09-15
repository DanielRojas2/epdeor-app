from django.db import models
from .Estante import Estante
from .Nivel import Nivel

class EstanteNivel(models.Model):
    ESTADO_CHOICES = (
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
    )
    estante = models.ForeignKey(Estante, on_delete=models.CASCADE)
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE)
    estado = models.CharField(max_length=8, choices=ESTADO_CHOICES)

    class Meta:
        verbose_name = "Estante Nivel"
        verbose_name_plural = "Estantes Niveles"

        constraints = [
            models.UniqueConstraint(
                fields=['estante', 'nivel'],
                name='unique_estante_nivel'
            )
        ]

    def __str__(self):
        return f"{self.estante} - {self.nivel}"

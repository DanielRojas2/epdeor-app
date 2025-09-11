from django.db import models
from .Departamento import Departamento
from .Unidad import Unidad

class Cargo(models.Model):
    nro_item = models.CharField(
        max_length=20, blank=False, null=False, primary_key=True
    )
    cargo = models.CharField(
        max_length=45, blank=False, null=False, unique=True
    )
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargo'
        constraints = [
            models.UniqueConstraint(
                fields=['departamento', 'unidad'],
                name='unique_departamento_unidad'
            )
        ]
        
    def __str__(self):
        return f"{self.nro_item}: {self.cargo} - {self.departamento}"
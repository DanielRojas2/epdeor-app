from django.db import models

class Personal(models.Model):
    ESTADO_CHOICES = (
        ('activo', 'activo'),
        ('inactivo', 'inactivo')
    )
    
    nombre_personal = models.CharField(max_length=25, blank=False, null=False)
    apellido_paterno = models.CharField(
        max_length=25, blank=False, null=False
    )
    apellido_materno = models.CharField(
        max_length=25, blank=False, null=False
    )
    estado = models.CharField(max_length=9, choices=ESTADO_CHOICES)
    
    class Meta:
        verbose_name = 'Personal'
        verbose_name_plural = 'Personal'
        
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'nombre_personal',
                    'apellido_paterno',
                    'apellido_materno'
                ],
                name='unique_nombre_apellidos'
            )
        ]
        
    def __str__(self):
        return f"{self.nombre_personal} {self.apellido_paterno} - {self.estado}"
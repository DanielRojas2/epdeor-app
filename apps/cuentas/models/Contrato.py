from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .Cargo import Cargo
from .Personal import Personal

class Contrato(models.Model):
    ESTADO_CHOICES = (
        ('activo', 'activo'),
        ('inactivo', 'inactivo')
    )
    nro_contrato = models.CharField(
        max_length=20, blank=False, null=False, primary_key=True
    )
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=8, choices=ESTADO_CHOICES)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    personal = models.ForeignKey(Personal, on_delete=models.CASCADE)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    
    @property
    def vigente(self):
        hoy = timezone.now().date()
        return self.fecha_inicio <= hoy <= self.fecha_fin
    
    def save(self, *args, **kwargs):
        self.estado = 'activo' if self.vigente else 'inactivo'
        
        if self.usuario:
            self.usuario.is_active = self.vigente
            self.usuario.save(update_fields=['is_active'])
    
    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
    
    def __str__(self):
        return f"Contrato: {self.nro_contrato} válido hasta el {self.fecha_fin}"
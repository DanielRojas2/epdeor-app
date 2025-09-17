from django import forms
from ..models.Contrato import Contrato

class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = [
            'nro_contrato',
            'estado',
            'cargo',
            'personal',
            'fecha_inicio',
            'fecha_fin',
            'estado'
        ]
        widgets = {
            'nro_contrato': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nro del contrato',
                    'autocomplete': 'off',
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'cargo': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'personal': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'usuario': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'fecha_inicio': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'fecha_fin': forms.DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            )
        }

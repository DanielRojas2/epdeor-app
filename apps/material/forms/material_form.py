from django import forms
from ..models.Material import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
            'material',
            'partida',
            'unidad_medida',
            'nivel_minimo',
            'cantidad_existente',
            'estado',
        ]
        widgets = {
            'material': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Material',
                    'autocomplete': 'off',
                }
            ),
            'partida': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'unidad_medida': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),
            'nivel_minimo': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'cantidad_existente': forms.NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            )
        }

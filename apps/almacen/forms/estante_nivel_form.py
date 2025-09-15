from django import forms
from ..models.EstanteNivel import EstanteNivel

class EstanteNivelForm(forms.ModelForm):
    class Meta:
        model = EstanteNivel
        fields = [
            'estante',
            'nivel',
            'estado',
        ]
        widgets = {
            'estante': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'nivel': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-select',
                }
            ),
        }

from django import forms
from ..models.Personal import Personal

class PersonalForm(forms.ModelForm):
    class Meta:
        model = Personal
        fields = [
            'nombre_personal',
            'apellido_paterno',
            'apellido_materno',
            'estado'
        ]
        widgets = {
            'nombre_personal': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Nombre del personal',
                    'autocomplete': 'off'
                }
            ),
            'apellido_paterno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido paterno',
                    'autocomplete': 'off'
                }
            ),
            'apellido_materno': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Apellido materno',
                    'autocomplete': 'off'
                }
            ),
            'estado': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            )
        }

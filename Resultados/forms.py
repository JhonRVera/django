from django.forms import ModelForm
from .models import Prediccion
from django import forms



INTEGER_CHOICES= [tuple([x,x]) for x in range(1,32)]
class PrediccionForm(ModelForm):
    class Meta:
        model = Prediccion
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'partido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Haz tu prediccion'}),
            'marcador': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Haz tu prediccion'}),
            'tarjetas': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Haz tu prediccion'}),
            'widget' : forms.Select(choices=INTEGER_CHOICES)
        }

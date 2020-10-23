from django import forms
from genero.models import Genero

class GeneroForm(forms.ModelForm):
    
    class Meta:
        model = Genero
        field = '__all__'
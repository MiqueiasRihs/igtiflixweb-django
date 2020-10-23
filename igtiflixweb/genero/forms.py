from django import forms

class GeneroForm(forms.Form):
    def __init__(self, *args, **kwards):
        super(GeneroForm, self).__init__(*args, **kwards)
        self.fields['descricao'].error_messages = {'required': 'Campo Obrigatório'}

    descricao = forms.CharField(label='Genero', required=True)
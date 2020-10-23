from django.shortcuts import render
from . import forms
from . import models

def cadastro(request):
    form = forms.GeneroForm()
    if request.method == 'POST':
        form = forms.GeneroForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print("ERROR")

    genero_list = models.Genero.objects.order_by('descricao')
    data_dict = {'form':form, 'genero_records':genero_list}
    return render(request, 'cadastro.html', data_dict)
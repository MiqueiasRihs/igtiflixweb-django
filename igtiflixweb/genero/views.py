from django.shortcuts import render
from . import forms

def cadastro(request):
    form = forms.GeneroForm()
    data_dict = {'form':form}
    return render(request, 'cadastro.html', data_dict)
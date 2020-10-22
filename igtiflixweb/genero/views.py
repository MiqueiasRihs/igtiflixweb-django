from django.shortcuts import render

def cadastro(request):
    return render(request, 'genero/cadastro.html')
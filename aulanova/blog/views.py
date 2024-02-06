from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    Novo_usuario = Usuario()
    Novo_usuario.nome = request.POST.get('nome')
    Novo_usuario.idade = request.POST.get('idade')
    Novo_usuario.save()

    usuarios = {
        'usuarios':Usuario.objects.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)
from django.shortcuts import render

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    Novo_usuario = Usuario()
    Novo_usuario.Nome = request.POST.get('nome')
    Novo_usuario.Idade = request.POST.get('idade')
    Novo_usuario.save()

    usuarios = {
        'usuarios':Usuario.object.all()
    }
    return render(request, 'usuarios/usuarios.html', usuarios)
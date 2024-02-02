from django.shortcuts import render

from AppCadUsuarios.models import Usuario


def home(request):
    return render(request, 'usuarios/home.html')
def usuarios(request):
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()
    # Exibir todos os usuários ja cadastrados em uma pagina
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    #retornar os dados para a página de listagem de usuarios
    return render(request, 'usuarios/usuarios.html',usuarios)

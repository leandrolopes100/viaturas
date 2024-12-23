from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #importando o formulário de criação de usuário
from django.contrib.auth.forms import AuthenticationForm #para a autenticação de usuários
from django.contrib.auth import authenticate, login, logout

# funão para pegar os dados do usuario e criar um novo usuário
def register_view(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login.html')
    else:
        user_form = UserCreationForm()
    return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password) #funcao do django para autenticar se senha e user ta certo
        if user is not None: #se o usuário nao for nulo
            login(request, user) # a função ja faz tudo automatico
            return redirect('cars_list')
            
        else: #senao retorna o form do autenticator
            login_form = AuthenticationForm()

    else:
         login_form = AuthenticationForm()
    return render (request, 'login.html', {'login_form': login_form})


def logout_view(request): #funcao para dar logoout
    logout(request) #parametro logout e dando um request
    return redirect('cars_list') #acabar a sessão e retornar para a lista de carros

    
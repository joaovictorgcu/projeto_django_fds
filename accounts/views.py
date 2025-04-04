from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Usuário já existe.')
            return render(request, 'register.html')

        User.objects.create_user(username=username, password=password1)
        messages.success(request, 'Usuário criado com sucesso!')
        return redirect('login')

    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('cars_list')  # redireciona para a página de carros, por exemplo
        else:
            messages.error(request, "Usuário ou senha inválidos.")

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('cars_list')
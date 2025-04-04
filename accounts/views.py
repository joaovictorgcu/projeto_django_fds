from django.contrib.auth.models import User
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

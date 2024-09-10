import random
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def log(request):
    if request.user.is_authenticated:
        return redirect('log')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'El usuario no existe')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Ingresaste correctamente')
            return redirect('home')
        else:
            messages.error(request, 'nombre de usuario o contraseña incorrectos')

    return render(request, 'log.html')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def logout_user(request):
    logout(request)
    messages.error(request, 'Sesion cerrada correctamente')
    return redirect('log')

@login_required
def intrucciones(request):
    return render(request, 'instrucciones.html')

@login_required
def niveles(request):
    return render(request, 'niveles.html')

@login_required
def coms(request):
    abecedario = [chr(i) for i in range(65, 91)] 
    return render(request, 'coms.html', {'abecedario': abecedario})

@login_required
def nivel_1(request):
    abecedario = [chr(i) for i in range(65, 91)] 
    return render(request, 'nivel_1.html', {'abecedario': abecedario})

@login_required
def nivel_2(request):
    letras = ['N', 'O', 'P', 'I', 'Ñ', 'A', 'X', 'L', 'T', 'Z', 'W']
    return render(request, 'nivel_2.html', {'letras': letras})

@login_required
def nivel_3(request):
    abecedario = [chr(i) for i in range(65, 91)] 
    random.shuffle(abecedario)
    lines = ['-'] * 26
    return render(request, 'nivel_3.html', {'abecedario': abecedario, 'lines': lines})
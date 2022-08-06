from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages

# Create your views here.

def logear(request):
    if request.method == 'POST':
        form = AuthenticationForm(request ,data=request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            usuario = authenticate(username = nombre_usuario, password = contraseña)
            if usuario is not None:
                login(request ,usuario)
                return redirect('Home')
            else:
                messages.error(request,'Usuario No Valido')
        else:
            messages.error(request,'Informacion Incorrecta')
    form = AuthenticationForm()
    return render(request,'Login/login.html',{'form':form})

def cerrar_session(request):
    logout(request)
    return redirect('Home')



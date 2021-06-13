from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'blank.html')

def usuarios(request):
    return render(request, 'usuarios.html')

def inventario(request):
    return render(request, 'inventario.html')

def gastos(request):
    return render(request, 'gastos.html')

def ventas(request):
    return render(request, 'ventas.html')

def clientes(request):
    return render(request, 'clientes.html')

def dashboard(request):
    return render(request, 'dashboard.html')

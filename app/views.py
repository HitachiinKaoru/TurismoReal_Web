from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'app/home.html')

def alojamientos(request):
    return render(request, 'app/alojamientos.html')

def servicios(request):
    return render(request, 'app/servicios.html')
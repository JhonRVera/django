from django.shortcuts import render
from .models import Prediccion
from .forms import PrediccionForm
# Create your views here.


def base(request):
    return render(request, 'frontend/principal.html')


def fasefinal(request):
    prediccion = PrediccionForm()
    context = {
        "prediccion": prediccion
    }

    if request.method == 'POST':
        pred = PrediccionForm(request.POST)

        if pred.is_valid():
            print('valido')
            predi = Prediccion()
            predi.nombre = pred.cleaned_data['nombre']
            predi.partido = pred.cleaned_data['partido']
            predi.marcador = pred.cleaned_data['marcador']
            predi.tarjetas = pred.cleaned_data['tarjetas']
            
            predi.save()
    return render(request, 'frontend/fasefinal.html', context)


def resultados(request):
    prediccion = Prediccion.objects.all()
    context = {
        "prediccion": prediccion
    }
    return render(request, 'frontend/tablaResultados.html', context)


def login(request):
    return render(request, 'frontend/login.html')

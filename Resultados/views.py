from django.shortcuts import render
# Create your views here.

def base(request):
    return render(request,'frontend/principal.html')

def listar(request):
    return render(request,'frontend/principal.html')

def fasegrupos(request):
    return render(request,'frontend/fasegrupos.html')

def fasefinal(request):
    return render(request,'frontend/fasefinal.html')

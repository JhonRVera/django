from django.shortcuts import render
# Create your views here.

def base(request):
    return render(request,'frontend/principal.html')

def listar(request):
    return render(request,'frontend/principal.html')
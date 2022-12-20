from django.urls import path
from .views import base,listar,fasegrupos,fasefinal,resultados,login

urlpatterns = [ 
    path('base/', base),
    path('listar/',listar),
    path('fasegrupos/',fasegrupos),
    path('fasefinal/',fasefinal),
    path('tablaResultados/',resultados),
    path('login/',login)
]
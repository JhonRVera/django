from django.urls import path
from .views import base,fasefinal,resultados,login

urlpatterns = [ 
    path('base/', base),
    path('fasefinal/',fasefinal),
    path('tablaResultados/',resultados),
    path('login/',login)
]
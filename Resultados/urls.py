from django.urls import path
from .views import base,listar,fasegrupos,fasefinal

urlpatterns = [ 
    path('base/', base),
    path('listar/',listar),
    path('fasegrupos/',fasegrupos),
    path('fasefinal/',fasefinal)
]
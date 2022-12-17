from django.urls import path
from .views import base,listar

urlpatterns = [ 
    path('base/', base),
]
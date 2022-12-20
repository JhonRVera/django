from django.db import models

# Create your models here.
class Prediccion(models.Model):
    nombre=models.CharField(max_length=10)
    partido= models.CharField(max_length=100)
    marcador=models.IntegerField()
    tarjetas=models.IntegerField()
    
    def __str__(self) :
        return self.nombre
from django.db import models

# Create your models here.
class Pais(models.Model):
    nombre_pais = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre_pais

class Sector (models.Model):
    nombre_sector = models.CharField(max_length=50)
    
    def __str__(self) -> str:
            return self.nombre_sector


class Personal (models.Model):
    nombre = models.CharField(max_length=50)    
    apellido = models.CharField(max_length=50)  
    nacimiento = models.DateField(null=True)    
    pais_origen = models.ForeignKey(Pais,on_delete=models.SET_NULL, null=True)
    sector = models.ForeignKey(Sector,on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return self.nombre
    

    

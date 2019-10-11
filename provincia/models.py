from django.db import models

# Create your models here.
class Provincia(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'provincias'
    
    def __str__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'ciudades'
    
    def __str__(self):
        return self.nombre
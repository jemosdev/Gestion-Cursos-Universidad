from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo= models.CharField(primary_key=True, max_length= 10)
    nombre= models.CharField(max_length=50)
    creditos= models.PositiveSmallIntegerField()

    #how to show the information in admin console
    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.nombre, self.creditos)
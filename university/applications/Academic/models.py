from django.db import models

# Create your models here.

class Curso(models.Model):
    codigo= models.CharField(primary_key=True, max_length= 10)
    nombre= models.CharField(max_length=50)
    creditos= models.PositiveSmallIntegerField()

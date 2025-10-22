from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

class Titulo(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)

class Ejemplar(models.Model):
    titulo = models.ForeignKey(Titulo, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    tipo = models.CharField(max_length=10, choices=[('venta','Venta'),('prestamo','Préstamo')])

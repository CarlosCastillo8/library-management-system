from django.db import models

TIPO_CHOICES = [
        ('prestamo', 'Préstamo'),
        ('venta', 'Venta'),
    ]

ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('prestado', 'Prestado'),
        ('reservado', 'Reservado'),
        ('mantenimiento', 'En mantenimiento'),
        ('dañado', 'Dañado'),
    ]

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

class Titulo(models.Model):
    nombre = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20, unique=True)
    autores = models.ManyToManyField(Autor, related_name='titulos')
    fecha_publicacion = models.DateField(null=True, blank=True)


class Ejemplar(models.Model):
    titulo = models.ForeignKey(Titulo, on_delete=models.CASCADE)
    disponible = models.BooleanField(default=True)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    codigo_interno = models.CharField(max_length=50, unique=True, null=False, blank=False, default='N/A')
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='disponible')
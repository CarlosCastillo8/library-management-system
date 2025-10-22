from django.db import models
from apps.usuarios.models import Usuario

class Venta(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_venta = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    metodo_pago = models.CharField(max_length=20, 
                                choices=[('efectivo','Efectivo'),
                                        ('tarjeta','Tarjeta'),
                                        ('online','Online')])
    estado = models.CharField(max_length=20, default='Pendiente')

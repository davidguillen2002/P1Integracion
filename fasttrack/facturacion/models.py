from django.db import models
from proveedores.models import Proveedor

class Factura(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('pendiente', 'Pendiente'), ('pagado', 'Pagado')])
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Factura {self.id} - {self.proveedor.nombre}"

class Pago(models.Model):
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE)
    fecha_pago = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[('completo', 'Completo'), ('pendiente', 'Pendiente')])

    def __str__(self):
        return f"Pago {self.id} - Factura {self.factura.id}"
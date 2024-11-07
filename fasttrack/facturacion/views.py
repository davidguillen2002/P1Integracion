from django.shortcuts import render
from .models import Factura

def lista_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'facturacion/lista.html', {'facturas': facturas})

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('proveedores/', include('proveedores.urls')),  # Ruta para proveedores
    path('facturacion/', include('facturacion.urls')),  # Ruta para facturación
]

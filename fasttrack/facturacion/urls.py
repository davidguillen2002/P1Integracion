from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_facturas, name='lista_facturas'),  # Muestra todas las facturas
]


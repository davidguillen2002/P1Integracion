# facturacion/scripts.py

import csv
from facturacion.models import Factura, Proveedor

def procesar_csv_facturas(file_path):
    with open(file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if not row['monto'] or not row['fecha_creacion']:
                print(f"Factura {row['id']} tiene campos incompletos.")
                continue

            factura_existente = Factura.objects.filter(
                proveedor__nombre=row['proveedor'],
                monto=row['monto'],
                fecha_creacion=row['fecha_creacion']
            ).exists()

            if factura_existente:
                print(f"Factura duplicada: {row['id']}")
                continue

            proveedor, _ = Proveedor.objects.get_or_create(nombre=row['proveedor'])
            Factura.objects.create(
                proveedor=proveedor,
                monto=row['monto'],
                estado=row['estado'],
                fecha_creacion=row['fecha_creacion']
            )

    print("Archivo CSV procesado con éxito.")
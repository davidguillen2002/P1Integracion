import csv
import paramiko
from facturacion.models import Factura

def generar_csv_facturas():
    # Generación del archivo CSV
    with open('facturas.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'proveedor', 'monto', 'estado', 'fecha_creacion']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for factura in Factura.objects.all():
            writer.writerow({
                'id': factura.id,
                'proveedor': factura.proveedor.nombre,
                'monto': factura.monto,
                'estado': factura.estado,
                'fecha_creacion': factura.fecha_creacion
            })

    print("Archivo CSV generado: facturas.csv")

    # Transferencia del archivo mediante SFTP
    transferir_archivo_sftp('facturas.csv', 'C:/Users/david/Downloads/RebexTinySftpServer-Binaries-Latest/data', '172.31.86.56 ', 22, 'tester', 'password')


def transferir_archivo_sftp(local_path, remote_path, hostname, port, username, password):
    try:
        # Configuración de la conexión SFTP
        transport = paramiko.Transport((hostname, port))
        transport.connect(username=username, password=password)

        # Inicia el cliente SFTP y transfiere el archivo
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_path, remote_path)
        print(f"Archivo {local_path} transferido exitosamente a {remote_path} en {hostname}.")

    except Exception as e:
        print(f"Error en la transferencia SFTP: {e}")
    finally:
        transport.close()

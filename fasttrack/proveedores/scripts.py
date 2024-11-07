import csv
import paramiko
from facturacion.models import Factura

# Detalles del servidor SFTP
SFTP_HOST = '172.31.86.56'
SFTP_PORT = 22
SFTP_USER = 'tester'
SFTP_PASS = 'password'
SFTP_REMOTE_PATH = 'data/facturas.csv'  # Ruta en el servidor SFTP relativa al directorio raíz del usuario

def generar_csv_facturas():
    # Generación del archivo CSV
    local_csv_path = 'facturas.csv'  # Ruta del archivo CSV en el sistema local
    with open(local_csv_path, 'w', newline='') as csvfile:
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

    print(f"Archivo CSV generado: {local_csv_path}")

    # Transferencia del archivo mediante SFTP
    if transferir_archivo_sftp(local_csv_path, SFTP_REMOTE_PATH):
        print("Archivo transferido correctamente al servidor SFTP.")
    else:
        print("Error al transferir el archivo al servidor SFTP.")


def transferir_archivo_sftp(local_path, remote_path):
    transport = None
    sftp = None
    try:
        # Configuración de la conexión SFTP
        transport = paramiko.Transport((SFTP_HOST, SFTP_PORT))
        transport.connect(username=SFTP_USER, password=SFTP_PASS)

        # Inicia el cliente SFTP y transfiere el archivo
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_path, remote_path)
        print(f"Archivo {local_path} transferido exitosamente a {remote_path} en {SFTP_HOST}.")
        return True

    except Exception as e:
        print(f"Error en la transferencia SFTP: {e}")
        return False

    finally:
        # Cerrar el cliente SFTP y el transporte si están abiertos
        if sftp:
            sftp.close()
        if transport:
            transport.close()
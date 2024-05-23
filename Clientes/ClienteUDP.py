import socket
import time

def send_udp_packets(host, port, interval, group_name, num_packets):
    # Crear un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_address = (host, port)

    for i in range(num_packets):
        try:
            # Crear el mensaje identificatorio único
            message = f'{group_name}-{i}'
            print(f'Enviando: {message}')
            
            # Enviar el mensaje
            sock.sendto(message.encode(), server_address)

            # Esperar el intervalo de tiempo configurado antes de enviar el siguiente paquete
            time.sleep(interval)

        except Exception as e:
            print(f'Error al enviar el paquete: {e}')
            break

    print('Finalizado el envío de paquetes')
    sock.close()

# Configuración
host = '127.0.0.1'       # Dirección IP del servidor
port = 9000              # Puerto del servidor
interval = 2             # Intervalo de tiempo en segundos
group_name = 'MPP'       # Nombre del grupo
num_packets = 10         # Número de paquetes a enviar

send_udp_packets(host, port, interval, group_name, num_packets)

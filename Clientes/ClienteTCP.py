import socket
import time

#RUN python ClienteTCP.py

def send_tcp_packets(host, port, interval, group_name, num_packets):
    try:
        # Crear un socket TCP/IP
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conectar el socket al servidor
        server_address = (host, port)
        print(f'Conectando a {host} en el puerto {port}')
        sock.connect(server_address)

        for i in range(num_packets):
            try:
                # Crear el mensaje identificatorio único
                message = f'{group_name}-{i}'
                print(f'Enviando: {message}')
                
                # Enviar el mensaje
                sock.sendall(message.encode())

                # Esperar el intervalo de tiempo configurado antes de enviar el siguiente paquete
                time.sleep(interval)

            except Exception as e:
                print(f'Error al enviar el paquete: {e}')
                break

    except Exception as e:
        print(f'No se pudo conectar al servidor: {e}')
    
    finally:
        print('Cerrando la conexión')
        sock.close()

# Configuración
host = '127.0.0.1'       # Dirección IP del servidor (LOCALHOST)
port = 9000              # Puerto del servidor
interval = 2             # Intervalo de tiempo en segundos
group_name = 'MPP'       # Nombre del grupo
num_packets = 10         # Número de paquetes a enviar

send_tcp_packets(host, port, interval, group_name, num_packets)

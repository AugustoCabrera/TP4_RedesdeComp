import socket

def start_udp_server(host, port):
    # Crear un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # Enlazar el socket a la dirección y puerto
    server_address = (host, port)
    print(f'Iniciando servidor en {host} en el puerto {port}')
    sock.bind(server_address)
    
    while True:
        print('Esperando paquetes...')
        data, address = sock.recvfrom(1024)
        
        if data:
            print(f'Recibido {data.decode()} desde {address}')

# Configuración
host = '127.0.0.1'  # Dirección IP del servidor
port = 9000         # Puerto del servidor

start_udp_server(host, port)

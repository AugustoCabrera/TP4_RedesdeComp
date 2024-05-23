import socket

#RUN  python ServerTCP.py

def start_tcp_server(host, port):
    # Crear un socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Enlazar el socket a la dirección y puerto
    server_address = (host, port)
    print(f'Iniciando servidor en {host} en el puerto {port}')
    server_socket.bind(server_address)
    
    # Escuchar por conexiones entrantes
    server_socket.listen(1)
    
    while True:
        print('Esperando conexión...')
        connection, client_address = server_socket.accept()
        
        try:
            print(f'Conexión desde {client_address}')
            
            # Recibir los datos en pequeños fragmentos y retransmitirlos
            while True:
                data = connection.recv(1024)
                if data:
                    print(f'Recibido: {data.decode()}')
                else:
                    print('No hay más datos desde', client_address)
                    break
                
        except Exception as e:
            print(f'Error en la conexión: {e}')
        
        finally:
            # Cerrar la conexión
            connection.close()

# Configuración
host = '127.0.0.1'  # Dirección IP del servidor (LOCALHOST)
port = 9000         # Puerto del servidor

start_tcp_server(host, port)

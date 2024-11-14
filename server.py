import socket

def init_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(1)
    print("Servidor iniciado en localhost:5000")
    while True:
        try:
            client_socket, address = server_socket.accept()
            print(f"Cliente conectado desde {address}")
            while True:
                data = client_socket.recv(1024).decode('utf-8')
                if not data:
                    break
                print(f"Mensaje recibido: {data}")
                if data == "DESCONEXION":
                    print("Cliente solicitó desconexión")
                    client_socket.close()
                    break
                response = data.upper()
                client_socket.send(response.encode('utf-8'))
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    init_server()
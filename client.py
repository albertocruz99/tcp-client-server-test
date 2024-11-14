import socket

def init_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 5000))
        print("Conectado al servidor")
        while True:
            message = input("Ingrese un mensaje (o 'DESCONEXION' para salir): ")
            client_socket.send(message.encode('utf-8'))
            if message == "DESCONEXION":
                print("Desconectando del servidor...")
                break
            response = client_socket.recv(1024).decode('utf-8')
            print(f"Respuesta del servidor: {response}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    init_client()
import socket
import threading

clients = {}
usernames = {}

def broadcast(message, client_socket):
    for client in clients.values():
        if client != client_socket:
            client.send(message)

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Mensagem recebida: {message.decode('utf-8')}")
                broadcast(message, client_socket)
            else:
                remove(client_socket)
                break
        except:
            remove(client_socket)
            break

def remove(client_socket):
    if client_socket in clients.values():
        username = [user for user, sock in clients.items() if sock == client_socket][0]
        del clients[username]

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 12345))
    server_socket.listen()

    print("Servidor aguardando conexões...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Uma conexão com {client_address} foi iniciada.")

        # Get the username
        client_socket.send("Você entrou na sala.".encode('utf-8'))
        username = client_socket.recv(1024).decode('utf-8')
        clients[username] = client_socket

        print(f"Nome do usuario do clinete é: {username}")
        thread = threading.Thread(target=handle_client, args=(client_socket,))
        thread.start()

if __name__ == "__main__":
    main()

import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(message.decode('utf-8'))
            else:
                break
        except:
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    username = input("Digite seu nome: ")
    client_socket.send(username.encode('utf-8'))

    thread = threading.Thread(target=receive_messages, args=(client_socket,))
    thread.start()

    while True:
        message = input("")
        full_message = f"[{username}]-> {message}"
        client_socket.send(full_message.encode('utf-8'))

if __name__ == "__main__":
    main()

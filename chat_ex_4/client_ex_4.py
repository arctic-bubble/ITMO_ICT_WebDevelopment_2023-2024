import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = "127.0.0.1"
server_port = 80
client_socket.connect((server_host, server_port))

def send_message():
    while True:
        message = input()
        client_socket.send(message.encode("utf-8"))

def receive_message():
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            print(message)
        except:
            client_socket.close()
            break

send_thread = threading.Thread(target=send_message)
receive_thread = threading.Thread(target=receive_message)

send_thread.start()
receive_thread.start()

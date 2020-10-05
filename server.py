# This is a chat app built around sockets in python
import socket
import time

# parameters for connection
SERVER_HOST = "0.0.0.0"
SERVER_PORT = 80
BUFFER_SIZE = 1024

# create socket
s = socket.socket()
print(f"[*] Listening at {SERVER_HOST}:{SERVER_PORT}")
s.bind((SERVER_HOST, SERVER_PORT))
s.listen(5)
client_socket, client_addr = s.accept()
print(f"[+] Connected to {client_addr}! \nReady to chat on Encrypted Channel \n\n")


def msg():

    def receive():
        while True:
            msgs = client_socket.recv(BUFFER_SIZE).decode()
            if msgs != "r":
                print(f"-->  {msgs}")
            elif msgs == "r":
                send()

    def send():
        while True:
            msgs = input("Type Message > ")
            client_socket.send(msgs.encode())
            if msgs == "end":
                exit()
            elif msgs == "r":
                receive()
            send()

    send()


msg()


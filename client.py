# This is a chat app built around sockets in python
import socket
import time

# parameters for connection
SERVER_HOST = "192.168.43.150"
SERVER_PORT = 80
BUFFER_SIZE = 1024

# create socket
s = socket.socket()
print(f"[+] Connecting to {SERVER_HOST}:{SERVER_PORT}")
time.sleep(3)
s.connect((SERVER_HOST, SERVER_PORT))
print("Connected! Ready to Chat on Encrypted Channel \n\n")


def msg():

    def receive():
        while True:
            msgs = s.recv(BUFFER_SIZE).decode()
            if msgs != "r":
                print(f"-->  {msgs}")
            elif msgs == "r":
                send()

    def send():
        while True:
            msgs = input("Type Message > ")
            s.send(msgs.encode())
            if msgs == "end":
                exit()
            elif msgs == "r":
                receive()
            send()

    receive()


msg()

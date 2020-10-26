import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
HOSTNAME = socket.gethostname()
print(SERVER)
print(HOSTNAME)
import socket
import threading

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DisconnectUser"

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_user(conn,addr):
    print(f"[CONNECTION] {addr} has connected")
    connected = True
    while connected:
        pass

def start():
    server.listen()
    print("[STATUS] Listening")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_user,args=(conn,addr))

start()

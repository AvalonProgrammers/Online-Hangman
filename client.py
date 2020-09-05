import socket

HEADER = 16
PORT = 5050
SERVER = input("Enter the ip address here.\n")
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DisconnectUser"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

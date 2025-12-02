import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 54321  # match your sender/PlugData port
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print("Listening on UDP", UDP_IP, "port", UDP_PORT)

while True:
    data, addr = sock.recvfrom(1024)
    print("Received from", addr, ":", data)
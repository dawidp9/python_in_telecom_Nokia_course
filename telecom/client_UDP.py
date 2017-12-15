from socket import socket, AF_INET, SOCK_DGRAM

IP = '127.0.0.1'
PORT = 5556

s = socket(AF_INET, SOCK_DGRAM)
s.settimeout(None)

while True:
    message = raw_input("input: ")
    s.sendto(message, (IP, PORT))
    print s.recv(1024)



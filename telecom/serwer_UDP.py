from socket import socket, AF_INET, SOCK_DGRAM

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5556

s = socket(AF_INET, SOCK_DGRAM)
s.bind((SERVER_HOST, SERVER_PORT))
s.settimeout(None)

while True:
    data, addr = s.recvfrom(1024)  # buffer size is 1024 bytes
    if data == "Kto jest prezydentem Polski?":
        s.sendto("Andrzej Duda ziomeczku", addr)
    else:
        s.sendto(data, addr)
    print "message: " + data

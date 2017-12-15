from socket import socket, AF_INET, SOCK_STREAM

IP = '127.0.0.1'
PORT = 5554
BUFFER_SIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.connect((IP, PORT))
print "connect to server " + str(IP) + ":" + str(PORT)

while True:
    message = raw_input("input: ")
    if message.strip() == "quit":
        s.send(message)
        print "disconnect form server " + str(IP) + ":" + str(PORT)
        break
    else:
        s.send(message)
        print s.recv(BUFFER_SIZE)
s.close()




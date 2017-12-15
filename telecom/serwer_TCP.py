from socket import socket, AF_INET, SOCK_STREAM

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5554
BUFFER_SIZE = 1024

s = socket(AF_INET, SOCK_STREAM)
s.bind((SERVER_HOST, SERVER_PORT))
print "Server up"
s.listen(2)

#echo serwer
try:
    while True:
        connection, addr = s.accept()
        print "client: " + str(addr) + " connected"
        while True:
            data = connection.recv(BUFFER_SIZE)
            if data.strip() == "quit":
                print "client: " + str(addr) + " disconnect"
                connection.shutdown(1)
                connection.close()
                break
            elif data:
                connection.send(data)
                print data, addr
except KeyboardInterrupt:
    s.close()
    print "Server down"

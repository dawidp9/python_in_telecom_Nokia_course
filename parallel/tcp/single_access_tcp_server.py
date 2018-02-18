"""
Initial module to be refactored during parallelism exercises
    Refactor single-access to multi-access servers

:author: 'Grzegorz Latuszek (Nokia)'
"""
from select import select
import socket


class TcpServer(object):
    def __init__(self, port, host='localhost'):
        self.server_sock = TcpServer.create_server_socket(host, port)
        self.connections = [self.server_sock]

    @staticmethod
    def create_server_socket(host, port):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen(1)
        print('TCP server listening at', server_socket.getsockname())
        return server_socket

    def run(self):
        print "server running"
        try:
            while True:
                read_sockets, _, _ = select(self.connections, [], [])
                for sock in read_sockets:
                    if sock == self.server_sock:
                        self.handle_incomming_client(sock)
                    else:
                        self.handle_existing_client(sock)
        except KeyboardInterrupt:  # allow server to be stopped by Ctrl-C
            pass

    def handle_incomming_client(self, server_sock):
        # accept client, create dedicated socket for dialog-with-client
        client_connection_socket, client_addr = server_sock.accept()
        print('Connected client from {0}'.format(client_addr))
        self.connections.append(client_connection_socket)
        # self.handle_client(client_connection_socket)

    def handle_client(self, client_connection_socket):
        client_still_connected = True
        while client_still_connected:
            client_still_connected = self.handle_existing_client(client_connection_socket)

    def handle_existing_client(self, client_connection_socket):
        client_still_connected = True
        data = None
        READ_BUFFER_SIZE = 4096
        try:
            data = client_connection_socket.recv(READ_BUFFER_SIZE)
            if not data:
                client_still_connected = False
        except socket.error as sock_err:
            if sock_err.errno == 10054:  # An existing connection was forcibly closed by the remote host
                client_still_connected = False
            elif sock_err.message == 'timed out':
                pass
            else:
                raise
        if not client_still_connected:
            self.handle_leaving_client(client_connection_socket)
        else:
            try:
                if data:
                    self.handle_client_data(client_connection_socket, data)
                else:
                    self.handle_no_client_data_at_timeout(client_connection_socket)
            except socket.error as sock_err:
                if sock_err.errno == 10054:  # An existing connection was forcibly closed by the remote host
                    client_still_connected = False

        return client_still_connected

    def handle_leaving_client(self, client_connection_socket):
        client_addr = client_connection_socket.getpeername()
        print('Disconnected client {}'.format(client_addr))
        client_connection_socket.close()
        self.connections.remove(client_connection_socket)

    def handle_client_data(self, client_connection_socket, client_data):
        """ Derived classes should do something with client's data """
        pass

    def handle_no_client_data_at_timeout(self, client_connection_socket):
        """ Derived classes may send something to client while client is silent """
        pass

    def shutdown(self):
        self.server_sock.close()


class EchoServer(TcpServer):
    """
    Just send client's data back to client
    """
    def handle_client_data(self, client_connection_socket, client_data):
        echo = client_data.strip()
        if echo:
            client_addr = client_connection_socket.getpeername()
            print("echoing '{0}' back to client {1}".format(client_data.strip(), client_addr))
            client_connection_socket.send(client_data)


if __name__ == '__main__':
    host = 'localhost'
    port = 9641
    print "starting ECHO server at TCP %s:%s" % (host, port)
    server = EchoServer(port, host)
    server.run()

    print "server is going down"
    server.shutdown()
    print "server is down"
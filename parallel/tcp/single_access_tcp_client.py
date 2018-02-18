"""
Tool to be used during parallelism exercises
    Library to build derived Tcp clients or use TcpConnection as context manager

:author: 'Grzegorz Latuszek (Nokia)'
"""
import socket


class TcpClient(object):
    def __init__(self, port, host='localhost'):
        self.host = host
        self.port = port
        self.client_sock = self.create_client_socket()
        self.is_running = False

    def create_client_socket(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        return client_socket

    def connect(self):
        # TCP client must connect to TCP server
        self.client_sock.connect((self.host, self.port))

    def shutdown(self):
        self.client_sock.close()

    def send(self, data):
        self.client_sock.send(data)

    def receive(self):
        data = None
        connection_still_open = True
        READ_BUFFER_SIZE = 4096
        try:
            data = self.client_sock.recv(READ_BUFFER_SIZE)
            if not data:
                connection_still_open = False
        except socket.error as sock_err:
            if sock_err.errno == 10054:  # An existing connection was forcibly closed by the remote host
                data = None
                connection_still_open = False
            else:
                raise
        return data, connection_still_open

    def run(self):
        try:
            self.connect()
            self.handle_establishing_connection()
            self.enter_events_loop()

        except KeyboardInterrupt:  # allow it to be stopped by Ctrl-C
            pass
        finally:
            self.shutdown()

    def enter_events_loop(self):
        self.is_running = True
        while self.is_running:
            self.handle_event_loop_tick()

    def handle_establishing_connection(self):
        """ Derived classes may do something just after establishing connection to server """
        pass

    def handle_event_loop_tick(self):
        """ Derived classes may do something "at tick" of client event loop
        Base class just quits event loop """
        self.is_running = False


class TcpConnectonClosed(Exception):
    pass


class TcpConnection(TcpClient):
    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self.shutdown()
        if isinstance(exception_value, TcpConnectonClosed):
            return True  # we are ok with this
        else:
            return False  # other exception should be reraised

    def open(self):
        self.connect()

    def receive(self):
        data, connection_still_open = super(TcpConnection, self).receive()
        if not connection_still_open:
            raise TcpConnectonClosed
        return data

    def get_file_descriptor(self):
        return self.client_sock

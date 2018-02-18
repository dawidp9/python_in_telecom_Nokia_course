"""
Tool to be used during parallelism exercises
    Sends messages to connected client

:author: 'Grzegorz Latuszek (Nokia)'
"""
import argparse
import json
import random
from single_access_tcp_server import TcpServer


# ----------------------------------- input parameters parsing ---------------------------------------------------------
def get_options():
    parser = argparse.ArgumentParser(description='Message sender')

    # required
    parser.add_argument("--port",  type=int, required=True, help="port of sender")
    # optional
    parser.add_argument("--host", default="localhost", help="IP of machine running message sender (default: localhost)")

    return parser.parse_args()
# ----------------------------------------------------------------------------------------------------------------------


class MsgSender(TcpServer):
    def __init__(self, port, host='localhost'):
        super(MsgSender, self).__init__(port, host)
        self.rrc_messages = MsgSender.load_messages("ue_attach.json")
        self.messages_to_send = []

    @staticmethod
    def load_messages(messages_filename):
        messages = []
        with open(messages_filename) as msg_file:
            messages = json.load(msg_file)
        rrc_messages = [msg['_source']['layers']['lte_rrc'] for msg in messages]
        return rrc_messages

    def handle_incomming_client(self):
        # accept client, create dedicated socket for dialog-with-client
        client_connection_socket, client_addr = self.server_sock.accept()
        data_awaiting_timeout = 0.1 * random.randint(1, 10)
        client_connection_socket.settimeout(data_awaiting_timeout) # make client read timeoutable
        print('Connected client from {}'.format(client_addr))
        self.messages_to_send = self.rrc_messages[:]
        self.handle_client(client_connection_socket)

    def handle_no_client_data_at_timeout(self, client_connection_socket):
        if self.messages_to_send:
            msg = self.messages_to_send.pop(0)
            self.send_message(client_connection_socket, msg)

    def send_message(self, client_connection_socket, message):
        msg_json_str = json.dumps(message)
        client_connection_socket.send(msg_json_str)


if __name__ == "__main__":
    options = get_options()

    print("starting MsgSender server at TCP %s:%s" % (options.port, options.host))
    server = MsgSender(options.port, options.host)
    server.run()

    print("server is going down")
    server.shutdown()
    print("server is down")

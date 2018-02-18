from single_access_tcp_msg_sender import MsgSender
import concurrent.futures
import logging, sys


def run_msg_server(port):
    logger = logging.getLogger('MsgSender.{}'.format(port))
    logger.info("starting MsgSender servers at TCP port {}".format(port))
    server = MsgSender(port)
    server.run()
    logger.info("server at port {} going down".format(port))
    server.shutdown()

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s %(name)20s: %(message)s',
        stream=sys.stderr,
    )
    logger = logging.getLogger('main')

    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as server_pool:
        server_pool.map(run_msg_server, [9991, 9992, 9993, 9994])

    logger.info("servers down")


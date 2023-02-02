from typing import Iterable

import grpc
import socket

from gen import user_pb2
from gen import user_pb2_grpc


USER = '*'
PASSWORD = '*'


def get_socket() -> socket.socket:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('authserver.sit.edu.cn', 443))

    return s


GLOBAL_SOCKET = get_socket()


TLS_SRV_SENT_COUNT = 0
TLS_CLI_RECV_COUNT = 0

def client_stream(credential: user_pb2.OaCredential) -> Iterable[user_pb2.ClientStream]:
    global TLS_SRV_SENT_COUNT

    first_message = user_pb2.ClientStream(credential=credential)
    yield first_message

    s = GLOBAL_SOCKET.dup()
    while True:
        buffer: bytes = s.recv(1024)
        if buffer:
            message = user_pb2.ClientStream(tls_stream=buffer)
            TLS_SRV_SENT_COUNT += len(buffer)
            yield message


def main():
    global TLS_CLI_RECV_COUNT

    channel = grpc.insecure_channel('127.0.0.1:8000')
    stub = user_pb2_grpc.UserServiceStub(channel)
    s = GLOBAL_SOCKET

    credential = user_pb2.OaCredential(account=USER, password=PASSWORD)
    call = stub.Login(client_stream(credential))
    for response in call:
        response: user_pb2.ServerStream = response

        if response.tls_stream:
            buf = response.tls_stream
            if buf:
                s.send(buf)
                TLS_CLI_RECV_COUNT += len(buf)
        elif response.user:
            print('user = ', response)
            print('account = ', response.user.account)
            print('uid = ', response.user.uid)
            break

    GLOBAL_SOCKET.close()
    channel.close()

    print('client_stream exited, tls_srv_sent_count = ' + str(TLS_SRV_SENT_COUNT))
    print('server_stream exited, tls_cli_recv_count = ' + str(TLS_CLI_RECV_COUNT))


if __name__ == '__main__':
    main()

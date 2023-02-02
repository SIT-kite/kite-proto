import grpc

from gen import ping_pb2
from gen import ping_pb2_grpc


def main():
    with grpc.insecure_channel('localhost:8000') as channel:
        stub = ping_pb2_grpc.PingServiceStub(channel)

        request = ping_pb2.PingRequest(text='Hello world!')
        response = stub.Ping(request)
        print(response)


if __name__ == '__main__':
    main()

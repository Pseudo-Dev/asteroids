# import asyncio
import socket
from grpc import aio

import remote.transfer_pb2 as pb2
import remote.transfer_pb2_grpc as pb2g


def get_id():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    num = IP.split(".")[3]
    print(num)
    num -= 128
    return num


async def send():
    async with aio.insecure_channel('localhost:50505') as channel:
        stub = pb2g.TransferStub(channel)
        response = await stub.Xfer(pb2.Outbound(X=100, Y=100))
    print("Xfer client received: " + response.message)

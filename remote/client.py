import asyncio
import platform
from grpc import aio

import remote.transfer_pb2 as pb2
import remote.transfer_pb2_grpc as pb2g

name = platform.node()
print("########################")
print(name)
print("########################")


async def send():
    async with aio.insecure_channel('localhost:50505') as channel:
        stub = pb2g.TransferStub(channel)
        response = await stub.Xfer(pb2.Outbound(X=100, Y=100))
    print("Xfer client received: " + response.message)

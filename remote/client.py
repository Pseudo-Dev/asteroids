# import asyncio
import socket
from grpc import aio, insecure_channel, RpcError, StatusCode

import remote.asteroids_pb2 as pb2
import remote.asteroids_pb2_grpc as pb2g
import remote.config as config


peerDict = {}


def get_id():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    num = IP.split(".")[3]
    num = int(num) - config.first + 1
    return pb2.Peer(id=num, ip=IP)


def discover(me):
    for i in range(config.first, config.last):
        ip = config.netBase + str(i)
        if ip == me.ip:
            continue
        with insecure_channel(f'{ip}:50505') as channel:
            stub = pb2g.AsteroidsStub(channel)
            try:
                remote = stub.Discover(me, timeout=1)
            except RpcError as rpc_error:
                if rpc_error.code() in (StatusCode.CANCELLED,
                                        StatusCode.UNAVAILABLE,
                                        StatusCode.DEADLINE_EXCEEDED):
                    pass
                else:
                    print(f"#### Unknown RPC error: code={rpc_error.code()}")
                    print(f"message={rpc_error.details()}")
            else:
                if remote:
                    peerDict[remote.id] = remote.ip
                    # print(f'Client added {remote.id}: {remote.ip}')


async def send(asteroid, target):
    targetIP = peerDict[target]
    out = pb2.Outbound(X=int(asteroid.circle.getCenter().getX()),
                       Y=int(asteroid.circle.getCenter().getY()),
                       dX=asteroid.dX,
                       dY=asteroid.dY,
                       size=asteroid.size,
                       color=asteroid.color)
    async with aio.insecure_channel(f'{targetIP}:50505') as channel:
        stub = pb2g.AsteroidsStub(channel)
        try:
            await stub.Xfer(out, timeout=10)
        except Exception as e:
            print("######## POIKKEUS: " + str(e))

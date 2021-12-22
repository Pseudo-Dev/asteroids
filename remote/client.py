import asyncio
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


async def discovery(me):

    async def announce(me, ip):
        async with aio.insecure_channel(f'{ip}:50505') as channel:
            return await pb2g.AsteroidsStub(channel).Discover(me, timeout=2)

    reqs = []
    for i in range(config.first, config.last):
        ip = config.netBase + str(i)
        if ip == me.ip:
            continue
        reqs.append(announce(me, ip))
    peers = await asyncio.gather(*reqs, return_exceptions=True)
    for peer in peers:
        if not isinstance(peer, BaseException):
            peerDict[peer.id] = peer.ip
            print(f'Discovered peer {peer.id} at {peer.ip}')


async def send(asteroid, targetList):
    if not targetList:
        return
    out = pb2.Outbound(X=int(asteroid.circle.getCenter().getX()),
                       Y=int(asteroid.circle.getCenter().getY()),
                       dX=asteroid.dX,
                       dY=asteroid.dY,
                       size=asteroid.size,
                       color=asteroid.color)
    targetIP = peerDict[targetList[0]]
    async with aio.insecure_channel(f'{targetIP}:50505') as channel:
        stub = pb2g.AsteroidsStub(channel)
        try:
            print(f"Target: {targetIP}")
            await stub.Xfer(out, timeout=10)
        except Exception as e:
            print("######## POIKKEUS: " + str(e))

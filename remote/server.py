from concurrent import futures

import grpc
import remote.asteroids_pb2 as pb2
import remote.asteroids_pb2_grpc as pb2g
from remote.client import peerDict
from app.asteroid import Asteroid, asteroidList


class AsteroidsRPC(pb2g.AsteroidsServicer):

    # These implement the protocols from asteroids.proto

    def Discover(self, request, context):
        peerDict[request.id] = request.ip
        print(f'Peer {request.id} at {request.ip} discovered me')
        return myID

    def Xfer(self, request, context):
        print("Received one from " + context.peer())
        new = (Asteroid(X=request.X,
                        Y=request.Y,
                        dX=request.dX,
                        dY=request.dY,
                        size=request.size,
                        clr=request.color))
        asteroidList.append(new)
        return pb2.Success(result=True)


def serve(id, list):
    global myID, asteroidList   # The only way to pass these to the server
    myID = id
    asteroidList = list

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2g.add_AsteroidsServicer_to_server(AsteroidsRPC(), server)
    server.add_insecure_port('0.0.0.0:50505')   # TCP port 50505
    server.start()      # Starts a new thread and returns
    return server

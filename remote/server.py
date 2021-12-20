from concurrent import futures

import grpc
import remote.asteroids_pb2 as pb2
import remote.asteroids_pb2_grpc as pb2g

myID = None
asteroidList = []
peerList = []


class AsteroidsRPC(pb2g.AsteroidsServicer):

    def Discover(self, request, context):
        peerList[request.id] = request.ip
        print(f'Added {request.id} {request.ip}')
        return pb2.Peer(myID)

    def Xfer(self, request, context):
        # print("Received a MESSAGE!")
        return pb2.Success(result=True)


def serve(id, list):
    global myID, asteroidList
    myID = id
    asteroidList = list

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2g.add_AsteroidsServicer_to_server(AsteroidsRPC(), server)
    server.add_insecure_port('0.0.0.0:50505')
    server.start()
    return server

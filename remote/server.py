from concurrent import futures

import grpc
import remote.asteroids_pb2 as pb2
import remote.asteroids_pb2_grpc as pb2g


class AsteroidsRPC(pb2g.AsteroidsServicer):

    def Xfer(self, request, context):
        print("Received a MESSAGE!")
        return pb2.Success(result=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2g.add_AsteroidsServicer_to_server(AsteroidsRPC(), server)
    server.add_insecure_port('0.0.0.0:50505')
    server.start()
    return server

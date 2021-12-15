from concurrent import futures

import grpc
import remote.transfer_pb2 as pb2
import remote.transfer_pb2_grpc as pb2g


class Transfer(pb2g.TransferServicer):

    def Xfer(self, request, context):
        print("Received a MESSAGE!")
        return pb2.Success(result=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2g.add_TransferServicer_to_server(Transfer(), server)
    server.add_insecure_port('[::]:50505')
    server.start()

from concurrent import futures
import grpc
import stream_pb2
import stream_pb2_grpc
import cv2
import time
import numpy as np
import threading

class Listener(stream_pb2_grpc.StreamServicer):

    def __init__(self):
        self.frame = None

    def Detection(self, request, context):
        print(request)
        while True:
            yield stream_pb2.StreamFrame(frame=bytes([1,2,4,4]))
        # for i in request:
        #     print(i)
        #     yield image_pb2.AlertReply(reply=5)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    stream_pb2_grpc.add_StreamServicer_to_server(Listener(), server)
    
    server.add_insecure_port("0.0.0.0:50051")
    server.start()
    try:
        while True:
            print(f"Server on threads {threading.active_count()}")
            time.sleep(2)
    except KeyboardInterrupt:
        print("Keyboard Interrupt")
        server.stop(0)

if __name__ == "__main__":
    serve()
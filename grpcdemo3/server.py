from concurrent import futures
import math
import time
import grpc
import train_pb2_grpc, train_pb2


class TrainService(train_pb2_grpc.TrainServiceServicer):
    def __init__(self):
        pass

    def LoadDataSet(self, request, context):
        name = request.name
        content = request.content
        message = request.message
        try:
            filename = "/home/lynxi/" + name
            with open(filename, mode='wb') as f:
                f.write(content)
            status = train_pb2.Status(code=0, message="")
            return train_pb2.DataPrepareResponse(status=status)
        except Exception as e:
            status = train_pb2.Status(code=0, message=str(e))
            return train_pb2.DataPrepareResponse(status=status)

    def Train(self, request, context):
        try:
            lr = request.parameters.lr
            epoch = request.parameters.epoch
            batch = request.parameters.batch

            print("lr:", lr, "epoch:", epoch, "batch:", batch)

            status = train_pb2.Status(code=0, message="")
            responses = []
            responses.append(train_pb2.TrainResponse(status=status, content="begin training..."))
            responses.append(train_pb2.TrainResponse(status=status, content="begin training..."))
            responses.append(train_pb2.TrainResponse(status=status, content="completed training..."))

            for response in responses:
                yield response

        except Exception as e:
            status = train_pb2.Status(code=0, message=str(e))
            return train_pb2.TrainResponse(status=status)

    def Test(self, request, context):
        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    train_pb2_grpc.add_TrainServiceServicer_to_server(TrainService(), server)
    server.add_insecure_port('127.0.0.1:50052')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()

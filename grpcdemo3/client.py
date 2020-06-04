import grpc
import train_pb2_grpc, train_pb2


def run():
    channel = grpc.insecure_channel('127.0.0.1:50052')
    stub = train_pb2_grpc.TrainServiceStub(channel)
    print("------------------LoadDataSet------------------")

    filename = "./test.xls"

    contentByte = b''
    with open(filename, mode='rb') as f:
        contentByte = f.read()

    response = stub.LoadDataSet(train_pb2.DataPrepareRequest(name="aaa.xls", content=contentByte))
    print(response.status.code, " ", response.status.message)

    response = stub.Train(train_pb2.TrainRequest(
        parameters=train_pb2.Parameters(lr=0.5, epoch=4, batch=6)
    ))
    for item in response:
        print("Train called {code} at {message}".format(code=item.status.code, message=item.content))


if __name__ == '__main__':
    run()

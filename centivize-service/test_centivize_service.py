import sys
import grpc

# import the generated classes
import service.service_spec.centivize_service_pb2_grpc as grpc_ex_grpc
import service.service_spec.centivize_service_pb2 as grpc_ex_pb2

from service import registry

if __name__ == "__main__":

    try:
        test_flag = False
        if len(sys.argv) == 2:
            if sys.argv[1] == "auto":
                test_flag = True

        # Centivize Service
        endpoint = input("Endpoint (localhost:{}): ".format(registry["centivize_service"]["grpc"])) if not test_flag else ""
        if endpoint == "":
            endpoint = "localhost:{}".format(registry["centivize_service"]["grpc"])

        grpc_method = input("Method (summarize|similarity): ") if not test_flag else "summarize"

        # Open a gRPC channel
        channel = grpc.insecure_channel("{}".format(endpoint))
        stub = grpc_ex_grpc.CentivizeStub(channel)

        if grpc_method == "summarize":
            par = input("Paragraph: ") if not test_flag else "The dog is running and barking at the bear. The bear was sick, but he was still hungry. So he pounced at the dog. But the dog ran away. It was a really intense fight. Then a tiger and lion joined. The tiger joined the bear and the lion joined the dog. Who will win?"
            num = int(input("Number: ") if not test_flag else "11")
            pars = grpc_ex_pb2.Paragraph(par=par, num=num)
            response = stub.summarize(pars)
            print(response.value)
        elif grpc_method == "similarity":
            par1 = input("Paragraph 1: ") if not test_flag else "Hello. My name is Sam. I like to swim and eat cheese."
            par2 = input("Paragraph 2: ") if not test_flag else "Hello. My name is Bob. I hate swimming but I love pizza."
            pars = grpc_ex_pb2.Paragraphs(par1=par1, par2=par2)
            response = stub.similarity(pars)
            print(response.value)
        else:
            print("Invalid method!")
            exit(1)

    except Exception as e:
        print(e)
        exit(1)
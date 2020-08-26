import sys
import logging

import grpc
import concurrent.futures as futures

import service.common

# Importing the generated codes from buildproto.sh
import service.service_spec.centivize_service_pb2_grpc as grpc_bt_grpc
from service.service_spec.centivize_service_pb2 import Summary, Similarity

from service import summarize
from service import similarity

logging.basicConfig(level=10, format="%(asctime)s - [%(levelname)8s] - %(name)s - %(message)s")
log = logging.getLogger("centivize_service")

# Create a class to be added to the gRPC server
# derived from the protobuf codes.
class CentivizeServicer(grpc_bt_grpc.CentivizeServicer):
    def __init__(self):
        self.par = ''
        self.num = 11
        summarize.setup()
        # Just for debugging purpose.
        log.debug("CentivizerServicer created")

    # The method that will be exposed to the snet-cli call command.
    # request: incoming data
    # context: object that provides RPC-specific information (timeout, etc).
    def summarize(self, request, context):
        # In our case, request is a Numbers() object (from .proto file)
        self.par = request.par
        self.num = request.num
        if self.num is None:
            self.num = 11

        # To respond we need to create a Result() object (from .proto file)
        self.result = Summary()

        self.result.value = summarize.summarize(self.par, self.num)
        log.debug("summarize({},{})={}".format(len(self.par), self.num, self.result.value))
        return self.result

    def similarity(self, request, context):
        self.par1 = request.par1
        self.par2 = request.par2

        self.result = Similarity()
        self.result.value = similarity.similarity(self.par1, self.par2)
        log.debug("similarity({},{})={}".format(self.par1, self.par2, self.result.value))
        return self.result

# The gRPC serve function.
#
# Params:
# max_workers: pool of threads to execute calls asynchronously
# port: gRPC server port
#
# Add all your classes to the server here.
# (from generated .py files by protobuf compiler)
def serve(max_workers=10, port=7777):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    grpc_bt_grpc.add_CentivizeServicer_to_server(CentivizeServicer(), server)
    server.add_insecure_port("[::]:{}".format(port))
    return server


if __name__ == "__main__":
    """
    Runs the gRPC server to communicate with the Snet Daemon.
    """
    parser = service.common.common_parser(__file__)
    args = parser.parse_args(sys.argv[1:])
    service.common.main_loop(serve, args)

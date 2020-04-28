from thrift.protocol import TJSONProtocol
from thrift.transport.THttpClient import THttpClient

from api import Hawk


def run():
    # Setup Connection
    transport = THttpClient("http://localhost:8080/thrift/hawk/json")
    protocol = TJSONProtocol.TJSONProtocol(transport)
    client = Hawk.Client(protocol)

    # Make API Call
    result = client.listBackends()
    for backend in result:
        print(backend)


if __name__ == "__main__":
    run()

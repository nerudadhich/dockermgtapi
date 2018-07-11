from models.network import NetworkViewModel

class Network:
    def __init__(self, client):
        self.client = client

    def all(self):
        network_list = []
        networks = self.client.networks.list()
        for network in networks:
            obj = NetworkViewModel(network)
            network_list.append(obj.__dict__)
        
        return network_list

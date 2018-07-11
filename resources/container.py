from models.container import ContainerViewModel

class Container:
    def __init__(self, client):
        self.client = client
    
    ## listing all container details
    def all(self):
        container_list = []
        containers = self.client.containers.list()
        for container in containers:
            obj = ContainerViewModel(container)
            container_list.append(obj.__dict__)
            
        return container_list

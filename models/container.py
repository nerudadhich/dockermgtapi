from models.image import ImageViewModel
from models.network import NetworkViewModel
from models.volume import VolumeViewModel

class ContainerViewModel:
    def __init__(self, container):
        self.id = container.id
        self.name = container.name
        self.labels = container.labels

        ## container stats
        self.cpu_stats = container.stats(stream=False)["cpu_stats"]
        self.network_stats = container.stats(stream=False)["networks"]
        self.memory_stats = container.stats(stream=False)["memory_stats"]
        self.storage_stats = container.stats(stream=False)["storage_stats"]

        ## serializing the image object
        if(container.image):
            self.image = ImageViewModel(container.image).__dict__
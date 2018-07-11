from models.volume import VolumeViewModel

class Volume:
    def __init__(self, client):
        self.client = client

    ## listing all volume details
    def all(self):
        volume_list = []
        volumes = self.client.volumes.list()
        for volume in volumes:
            obj = VolumeViewModel(volume)
            volume_list.append(obj.__dict__)
        
        return volume_list

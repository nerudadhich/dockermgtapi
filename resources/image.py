from models.image import ImageViewModel

class Image:
    def __init__(self, client):
        self.client = client

    def all(self):
        image_list = []
        images = self.client.images.list()
        for image in images:
            obj = ImageViewModel(image)
            image_list.append(obj.__dict__)
        
        return image_list

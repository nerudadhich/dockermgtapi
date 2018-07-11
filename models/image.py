class ImageViewModel:
    def __init__(self, image):
        self.id = image.id
        self.tags = image.tags
        self.labels = image.labels
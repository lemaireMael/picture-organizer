class ImageObj:

    def __init__(self, path, name, meta=None):
        self.path = path
        self.name = name
        self.meta = meta

    def __str__(self):
        return f"Nom : {self.name}, date : {self.meta}, chemin {self.path}"

    def get_img(self):
        return self.name, self.path, self.meta
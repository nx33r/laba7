class Camera:
    def __init__(self, model, resolution, zoom, memory_card_type, photos_count):
        self.model = model
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = photos_count

    def reset_zoom(self):
        self.zoom = 1.0

    def save_photo(self):
        self.photos_count += 1

    def erase_memory(self):
        self.photos_count = 0

    def change_settings(self, resolution, zoom):
        self.resolution = resolution
        self.zoom = zoom

    def get_model(self):
        return self.model

    def set_model(self, model):
        self.model = model

    def get_resolution(self):
        return self.resolution

    def set_resolution(self, resolution):
        self.resolution = resolution

    def get_zoom(self):
        return self.zoom

    def set_zoom(self, zoom):
        self.zoom = zoom

    def get_memory_card_type(self):
        return self.memory_card_type

    def set_memory_card_type(self, memory_card_type):
        self.memory_card_type = memory_card_type

    def get_photos_count(self):
        return self.photos_count

    def set_photos_count(self, photos_count):
        self.photos_count = photos_count


if __name__ == "__main__":
    camera = Camera("Canon", "1024x768", 1.0, "SD", 0)
    print("Model:", camera.get_model())
    print("Resolution:", camera.get_resolution())
    print("Zoom:", camera.get_zoom())
    print("Memory Card Type:", camera.get_memory_card_type())
    print("Photos Count:", camera.get_photos_count())

    camera.save_photo()
    print("Photos Count after saving a photo:", camera.get_photos_count())

    camera.reset_zoom()
    print("Zoom after resetting:", camera.get_zoom())

    camera.erase_memory()
    print("Photos Count after erasing memory:", camera.get_photos_count())

    camera.change_settings("2048x1536", 2.0)
    print("Resolution after changing settings:", camera.get_resolution())
    print("Zoom after changing settings:", camera.get_zoom())


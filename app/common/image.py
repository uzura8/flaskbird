from PIL import Image as pil_image

class Image():

    def __init__(self, path, size_infos):
        img = pil_image.open(path)
        self.img = img

    def crop_center(self, crop_width, crop_height):
        img_width, img_height = self.img.size
        return self.img.crop(((img_width - crop_width) // 2,
                             (img_height - crop_height) // 2,
                             (img_width + crop_width) // 2,
                             (img_height + crop_height) // 2))

    def crop_max_square(self):
            return self.crop_center(self, min(self.img.size), min(self.img.size))

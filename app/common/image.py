import os
import json
from PIL import Image as pil_image
from PIL.ExifTags import TAGS
from app.common.file import makedirs
from app.common.util import remove_bytes_value

class Image():

    def __init__(self, input_path, output_path='', remove_profile=True):
        mode = 'r'
        if not output_path:
            output_path = input_path
        self.remove_profile = remove_profile
        self.img = pil_image.open(input_path, mode)
        self.output_path = output_path
        dir_path = os.path.dirname(self.output_path)
        makedirs(dir_path)


    def resize(self, width, height, type='relative'):
        if type == 'crop':
            self.resize_square_crop(width)
        else:
            self.resize_relative(width, height)
        self.save()


    def get_exifs(self, format='json'):
        if format == 'json':
            return json.dumps(self.exifs)
        return self.exifs


    def save(self):
        if self.img.format == 'jpeg':
            if self.remove_profile:
                self.img.save(self.output_path, 'jpeg', quality=95)
            else:
                self.img.save(self.output_path, 'jpeg', quality=95,
                            icc_profile=self.img.info.get('icc_profile'))
        else:
            self.img.save(self.output_path)


    def resize_relative(self, width, height):
        self.img.thumbnail((width, height), pil_image.ANTIALIAS)


    def resize_square_crop(self, size):
        square_size = min(self.img.size)
        width, height = self.img.size
        if width > height:
            top = 0
            bottom = square_size
            left = (width - square_size) / 2
            right = left + square_size
            box = (left, top, right, bottom)
        else:
            left = 0
            right = square_size
            top = (height - square_size) / 2
            bottom = top + square_size
            box = (left, top, right, bottom)
        self.img = self.img.crop(box)
        self.img.thumbnail((size, size), pil_image.ANTIALIAS)

    def set_exifs(self):
        self.exifs = {}
        if self.img.format != 'jpeg':
            pass

        try:
            exif = self.img._getexif()
        except AttributeError:
            pass

        for tag_id, values in exif.items():
            values = remove_bytes_value(values)
            if values is None:
                continue
            tag = TAGS.get(tag_id, tag_id)
            self.exifs[tag] = values


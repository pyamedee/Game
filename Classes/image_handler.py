# -*- coding:Utf-8 -*-


class ImageHandler:
    def __init__(self, img_dictionary):
        self.d = img_dictionary

    def update(self, state):
        raise NotImplementedError

    def get_image(self, image_id):
        return self.d[image_id]

    def __getitem__(self, item):
        return self.get_image(item)



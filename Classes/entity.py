# -*- coding:Utf-8 -*-

import pyglet.sprite


class Entity:
    def __init__(self, sprite, image_handler):
        self.sprite = sprite
        self.image_handler = image_handler
        self.state = 'WALK;right'
        self.image_id = 0

    def update_position(self, x, y):
        self.sprite.position = x, y

    def update_image(self):
        image_id = self.image_handler.update(self.state)
        if image_id != self.image_id:
            self.image_id = image_id
            self.sprite.image = self.image_handler.get_image(image_id)

# -*- coding:Utf-8 -*-

import pyglet.sprite


class Entity:
    def __init__(self, sprite, image_handler):
        self.sprite = sprite
        self.image_handler = image_handler
        self.state = 'static'
        self.image_id = 0

        self.sprite.on_animation_end = self.on_animation_end

    def update_position(self, x, y):
        self.sprite.position = x, y

    def update_image(self):
        image_id = self.image_handler.update(self.state)
        if image_id != self.image_id:
            self.sprite.image = self.image_handler.get_image(image_id)

    def on_animation_end(self):
        self.sprite.image = self.image_handler.d[8209]

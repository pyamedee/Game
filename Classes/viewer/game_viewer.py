# -*- coding:Utf-* -*-

import pyglet
from .base_viewer import BaseViewer
from ..entity import Entity
from ..image_structure_data import ImageDictionary
from ..constants import *
from .player_image_handler import PlayerImageHandler


class GameViewer(BaseViewer):
    def __init__(self, config, model, window=None, *args, **kwargs):
        if not window:
            window = pyglet.window.Window(*args, **kwargs)
        super(GameViewer, self).__init__(model, window)

        self.batch = pyglet.graphics.Batch()

        self.entities = []

        self.bg_sprites = []
        self.bg_layers = [pyglet.graphics.OrderedGroup(i) for i in reversed(range(0, 22, 2))]
        #  inversé car la couche 10 est la plus au fond
        self.entity_layer = pyglet.graphics.OrderedGroup(17)

        self.img_dict = ImageDictionary(config['resources_path'])
        self.load_bg(BLACK_FOREST)

        sprite = pyglet.sprite.Sprite(self.img_dict[ENTITY | ROGUE | ATTACK],
                                      50, 62, batch=self.batch, group=self.entity_layer)
        img_handler = PlayerImageHandler(self.img_dict, ROGUE)
        self.player = Entity(sprite, img_handler)
        self.entities.append(self.player)

        self.window.set_handler('on_draw', self.on_draw)

    def load_bg(self, background_id):
        for i in range(11):
            layer_id = BG | background_id | (i + 1) * VARIATION
            sprite = pyglet.sprite.Sprite(self.img_dict[BG | BLACK_FOREST | layer_id],
                                          0, 0, batch=self.batch, group=self.bg_layers[i])
            self.bg_sprites.append(sprite)

    def on_draw(self, *args, **kwargs):
        self.batch.draw()
        self.window.set_caption(str(pyglet.clock.get_fps()))
        for entity in self.entities:
            entity.update_image()





# -*- coding:Utf-* -*-

import pyglet
from .base_viewer import BaseViewer
from ..entity import Entity
from ..image_handler import ImageHandler
from ..image_structure_data import ImageDictionary
from ..constants import *


class GameViewer(BaseViewer):
    def __init__(self, model, width, height, window=None, config=None):
        if not window:
            window = pyglet.window.Window(width=width, height=height, config=config)
        else:
            window.set_size(width, height)
        super(GameViewer, self).__init__(model, window)

        self.batch = pyglet.graphics.Batch()
        self.bg = pyglet.graphics.OrderedGroup(0)
        self.front = pyglet.graphics.OrderedGroup(1)

        self.img_dict = ImageDictionary('C:/Users/Hélène Le Berre/rp/Game/Resources')

        bg = pyglet.sprite.Sprite(self.img_dict[BG | BLACK_FOREST | LAYER10], 0, 0, batch=self.batch, group=self.bg)
        bg_handler = ImageHandler(self.img_dict)
        self.bg = Entity(bg, bg_handler)

        sprite = pyglet.sprite.Sprite(self.img_dict[ENTITY | ROGUE | ATTACK], 100, 100, batch=self.batch, group=self.front)
        img_handler = ImageHandler(self.img_dict)
        self.player = Entity(sprite, img_handler)

        self.window.set_handler('on_draw', self.on_draw)

    def on_draw(self, *args, **kwargs):
        self.batch.draw()
        self.window.set_caption(str(pyglet.clock.get_fps()))





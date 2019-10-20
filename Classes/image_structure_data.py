# -*- coding:Utf-8 -*-

import pyglet.image as pgimg
import pyglet.resource as pgres
from glob import glob
import os
from .constants import *


class ImageDictionary(dict):
    ENTITY = 0b0001
    BG = 0b0010
    PLATFORMS = 0b0011

    ROGUE = 0b0000_0001_0000
    WARRIOR = 0b0000_0010_0000
    MAGE = 0b0000_0011_0000

    ATTACK = 0b0000_0001_000000000000
    EXTRA_ATTACK = 0b0000_0010_000000000000
    CLIMB = 0b0000_0011_000000000000
    DEATH = 0b0000_0100_000000000000
    HIGH_JUMP = 0b0000_0101_000000000000
    HURT = 0b0000_0110_000000000000
    IDLE = 0b0000_0111_000000000000
    JUMP = 0b0000_1000_000000000000
    PUSH = 0b0000_1001_000000000000
    RUN = 0b0000_1010_000000000000
    RUN_ATTACK = 0b0000_1011_000000000000
    WALK = 0b0000_1100_000000000000
    WALK_ATTACK = 0b0000_1101_000000000000
    BASE = 0b0000_1110_000000000000

    BLACK_FOREST = ROGUE

    LAYER0 = ATTACK
    LAYER1 = EXTRA_ATTACK
    LAYER2 = CLIMB
    LAYER3 = DEATH
    LAYER4 = HIGH_JUMP
    LAYER5 = HURT
    LAYER6 = IDLE
    LAYER7 = JUMP
    LAYER8 = PUSH
    LAYER9 = RUN
    LAYER10 = RUN_ATTACK

    VARIATION = 4096
    FLIPPED = 524288

    def __init__(self, res_directory):
        super(ImageDictionary, self).__init__()
        pgres.path = ['Resources']
        pgres.reindex()
        self.res = res_directory
        self.anim_freq = 1 / 30

        options = {
            'Background': self.parse_bg,
            'Entity': self.parse_entity,
            'Platforms': self.parse_platforms
        }
        for folder in glob(self.res + '/*'):
            options[os.path.basename(folder)](folder)

    def parse_bg(self, folder):  # each layer can be accessed with BG | <MAP_NAME> | <LAYER_NUMBER>
        for bg in glob(folder + '/*'):
            with open(bg + '/.data', 'r') as data:
                bg_id = int(data.read())
            for i, layer in enumerate(glob(bg + '/*.png')):
                layer_id = (i + 1) * VARIATION
                image_id = BG | bg_id | layer_id
                self[image_id] = pgimg.load(layer)

    def parse_entity(self, folder):
        # each action can be accessed with ENTITY | <ENTITY_NAME> | <ACTION_NAME> (| FLIPPED)
        for entity in glob(folder + '/*'):
            with open(entity + '/.data', 'r') as data:
                entity_id = int(data.read())
            self[ENTITY | entity_id | BASE] = pgimg.load(entity + '/.base.png')
            self[ENTITY | entity_id | BASE | FLIPPED] = pgres.image(
                self.convert_path(entity + '/.base.png'), flip_x=True)

            for i, action in enumerate(glob(entity + '/*')):
                action_id = (i + 1) * VARIATION

                img_list = list()
                rimg_list = list()
                for img in glob(action + '/*.png'):
                    img_list.append(pgimg.load(img))
                    rimg_list.append(pgres.image(self.convert_path(img), flip_x=True))

                anim = pgimg.Animation.from_image_sequence(img_list, self.anim_freq, False)
                ranim = pgimg.Animation.from_image_sequence(rimg_list, self.anim_freq, False)
                self[ENTITY | entity_id | action_id] = anim
                self[ENTITY | entity_id | action_id | FLIPPED] = ranim

    @staticmethod
    def convert_path(path):
        i = path.index('Resources') + len('Resources/')
        relative_path = path.replace(path[:i], '')
        return relative_path.replace('\\', '/')

    def parse_platforms(self, folder):
        pass

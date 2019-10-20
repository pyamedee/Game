# -*- coding:Utf-* -*-

from ..constants import *
from ..image_handler import ImageHandler


class PlayerImageHandler(ImageHandler):
    def __init__(self, image_dict, entity_id):
        super(PlayerImageHandler, self).__init__(image_dict)
        self.entity_id = entity_id

    def update(self, state):
        """state should be <upper_action_name>;<direction>"""
        action_name, direction = state.split(';')
        action_id = getattr(self.d, action_name)

        if direction == 'right':
            return ENTITY | self.entity_id | action_id
        elif direction == 'left':
            return ENTITY | self.entity_id | action_id | FLIPPED
        raise ValueError(f'direction {direction} is not valid')


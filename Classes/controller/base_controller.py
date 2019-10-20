# -*- coding:Utf-8 -*-


class BaseController:
    def __init__(self, model, viewer):
        self.model = model
        self.viewer = viewer

# -*- coding:Utf-8 -*-

import pyglet


class BaseViewer:

    def __init__(self, model, window):
        self.window = window
        self.model = model

    def bind(self, event_manager):
        for name, handler in event_manager.handlers:
            self.window.set_handler(name, handler)

    def unbind(self, event_manager):
        for name, handler in event_manager.handlers:
            self.window.remove_handler(name, handler)



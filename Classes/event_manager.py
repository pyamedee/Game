# -*- coding:Utf-8 -*-


class EventManager:
    handlers = []

    def __init__(self, action_manager):
        self.action_manager = action_manager

    @classmethod
    def event(cls, func):
        cls.handlers.append((func.__name__, func))







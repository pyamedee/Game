# -*- coding:Utf-8 -*-


class ActionManager:
    def __init__(self):
        pass

    def do(self, action_name):
        getattr(self, action_name)()

# -*- coding:Utf-8 -*-

from ..event_manager import EventManager


class GameEventManager(EventManager):

    def __init__(self, action_manager, controls):
        super(GameEventManager, self).__init__(action_manager)
        self.controls = controls

    @EventManager.event
    def on_key_press(self, symbol, modifiers):
        self.action_manager.do(self.controls[symbol, modifiers])

    @EventManager.event
    def on_key_release(self, symbol, modifiers):
        self.action_manager.stop(self.controls[symbol, modifiers])



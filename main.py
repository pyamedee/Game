# -*- coding:Utf-8 -*-

from Classes import viewer, model, controller
from pyglet import app, gl, canvas
import json

if __name__ == '__main__':
    modes = canvas.get_display().get_default_screen().get_modes()
    with open('configs.json', 'r') as file:
        viewer.game_viewer.GameViewer(config=json.load(file), model=None, mode=modes[67])
    app.run()



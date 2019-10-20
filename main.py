# -*- coding:Utf-8 -*-

from Classes import viewer, model, controller
from pyglet import app, gl
import json

if __name__ == '__main__':
    with open('configs.json', 'r') as file:
        viewer.game_viewer.GameViewer(json.load(file), None, 1600, 800)
    app.run()



# -*- coding:Utf-8 -*-

from Classes import viewer, model, controller
from pyglet import app, gl

if __name__ == '__main__':
    viewer.game_viewer.GameViewer(None, 1600, 800)
    app.run()



from pico2d import *

class Background:
    # image = None

    def __init__(self):
        self.image = load_image('background.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(1250, 485, 2500, 1024)



from pico2d import *

class Maingrass:
    image = None

    def __init__(self):
        self.image = load_image('block_sheet.png')
        self.Wsize, self.Hsize = 50, 50

    def update(self):
        pass

    def draw(self):
        self.x, self.y = 25, 25
        for i in range(34):
            self.image.clip_draw(60, 250, 160, 160, self.x, self.y, self.Wsize, self.Hsize)
            self.x += 50
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 0, 0, 1600-1, 50
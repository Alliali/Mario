from pico2d import *

class Stair_block:
    image = None

    def __init__(self):
        if Stair_block.image == None:
            Stair_block.image = load_image('block_sheet.png')
        self.x, self.y = 1010, 232


    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(270, 250, 160, 160, self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())

class Item_block:
    image = None

    def __init__(self):
        if Item_block.image == None:
            Item_block.image = load_image('block_sheet.png')
        self.x, self.y = 50, 231

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(480, 450, 160, 160, self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())

class Broken_block:
    image = None

    def __init__(self):
        if Broken_block.image == None:
            Broken_block.image = load_image('block_sheet.png')
        self.x, self.y = 100, 231

    def get_bb(self):
        return self.x - 25, self.y - 25, self.x + 25, self.y + 25

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(270, 450, 160, 160, self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb())


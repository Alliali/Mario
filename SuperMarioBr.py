from pico2d import *

class Block:
    def __init__(self):
        self.image = load_image('block_sheet.png')

    def draw_floor(self):
        self.x, self.y = 25, 25
        for i in range(26):
            self.image.clip_draw(60, 250, 160, 160, self.x, self.y, 50, 50)
            self.x += 50
    def draw_stair(self):
        self.x, self.y = 350, 300
        self.image.clip_draw(270, 250, 160, 160, self.x, self.y, 50, 50)
    def draw_itemblock(self):
        self.x, self.y = 450, 300
        self.image.clip_draw(480, 450, 160, 160, self.x, self.y, 50, 50)
    def draw_brokenblock(self):
        self.x, self.y = 400, 300
        self.image.clip_draw(270, 450, 160, 160, self.x, self.y, 50, 50)


class Mario:
    def __init__(self):
        self.image = load_image('marios.png')
        self.x, self.y = 400, 80
        self.frame = 0

    def draw(self):
        self.image.clip_draw(275+self.frame * 15, 340, 15, 18, self.x, self.y, 60, 60)

    def update(self):
        self.x += mariomove * 10
        if self.y >= 80:
            self.y += mariojump * 5
        elif notjump == True:
            self.y = 80
        self.frame = (self.frame + 1) % 4

def handle_events():
    global inprogress
    global mariomove
    global mariojump
    global notjump
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            inprogress = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                mariomove -= 1
            elif event.key == SDLK_RIGHT:
                mariomove += 1
            elif event.key == SDLK_UP:
                notjump = False
                if notjump == False:
                    mariojump = 0
                mariojump += 5
            elif event.key == SDLK_ESCAPE:
                inprogress = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                mariomove += 1
            elif event.key == SDLK_RIGHT:
                mariomove -= 1
            elif event.key == SDLK_UP:
                notjump = True
                mariojump -= 10


open_canvas()

block = Block()
mario = Mario()

inprogress = True
notjump= True

mariomove = 0
mariojump = 0

while inprogress:

    handle_events()
    mario.update()
    clear_canvas()
    block.draw_floor()
    block.draw_stair()
    block.draw_itemblock()
    block.draw_brokenblock()
    mario.draw()
    update_canvas()


    delay(0.05)

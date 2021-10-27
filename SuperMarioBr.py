from pico2d import *

class Block:
    def __init__(self):
        self.image = load_image('block_sheet.png')
        self.Wblksize, self.Hblksize = 50, 50

    def draw_floor(self):
        self.x, self.y = 25, 25
        for i in range(26):
            self.image.clip_draw(60, 250, 160, 160, self.x, self.y, self.Wblksize, self.Hblksize)
            self.x += 50
    def draw_stair(self):
        self.x, self.y = 350, 300
        self.image.clip_draw(270, 250, 160, 160, self.x, self.y, self.Wblksize, self.Hblksize)
    def draw_itemblock(self):
        self.x, self.y = 450, 300
        self.image.clip_draw(480, 450, 160, 160, self.x, self.y, self.Wblksize, self.Hblksize)
    def draw_brokenblock(self):
        self.x, self.y = 400, 300
        self.image.clip_draw(270, 450, 160, 160, self.x, self.y, self.Wblksize, self.Hblksize)


class Mario:
    def __init__(self):
        self.image = load_image('marios.png')
        self.x, self.y = 400, 80
        self.mwsize, self.mhsize = 60, 60
        self.frame = 0

    def draw(self):
        if notmove == False:
            if rightmove == True:
                if notjump == False:
                    self.image.clip_draw(352, 340, 22, 18, self.x, self.y, self.mwsize, self.mhsize)
                elif notjump == True:
                    self.image.clip_draw(290+self.frame * 15, 340, 15, 18, self.x, self.y, self.mwsize, self.mhsize)
            elif rightmove == False:
                if notjump == False:
                    self.image.clip_draw(352, 340, 22, 18, self.x, self.y, self.mwsize, self.mhsize)
                elif notjump == True:
                    self.image.clip_draw(210 + self.frame * 15, 340, 15, 18, self.x, self.y, self.mwsize, self.mhsize)
        if notmove == True:
            if rightmove == True:
                if notjump == True:
                    self.image.clip_draw(275, 340, 15, 18, self.x, self.y, self.mwsize, self.mhsize)
                elif notjump == False:
                    self.image.clip_draw(352, 340, 22, 18, self.x, self.y, self.mwsize, self.mhsize)
            elif rightmove == False:
                if notjump == True:
                    self.image.clip_draw(222, 340, 15, 18, self.x, self.y, self.mwsize, self.mhsize)
                elif notjump == False:
                    self.image.clip_draw(140, 340, 19, 18, self.x, self.y, self.mwsize, self.mhsize)



    def update(self):
        self.x += mariomove * 10
        if self.y >= 80:
            self.y += mariojump * 5
        elif notjump == True:
            self.y = 80
        self.frame = (self.frame + 1) % 3

def handle_events():
    global inprogress
    global mariomove
    global mariojump
    global notjump
    global notmove
    global rightmove
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            inprogress = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                mariomove -= 1
                notmove = False
                rightmove = False
            elif event.key == SDLK_RIGHT:
                mariomove += 1
                notmove = False
                rightmove = True
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
                notmove = True
                rightmove = False
            elif event.key == SDLK_RIGHT:
                mariomove -= 1
                notmove = True
                rightmove = True
            elif event.key == SDLK_UP:
                notjump = True
                mariojump -= 10


open_canvas()

block = Block()
mario = Mario()

inprogress = True
notjump= True
notmove = True
rightmove = True

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


    delay(0.04)

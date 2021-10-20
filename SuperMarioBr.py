from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('mario_sheet.png')

    def draw(self):
        # self.image.draw(400, 150)
        self.x, self.y = 400, 30
        self.image.clip_draw(13,3,150,20,self.x,self.y,600,40)


class Mario:
    pass

def handle_events():
    global inprogress
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            inprogress = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            inprogress = False

open_canvas()

stonegrass = Grass()

inprogress = True

while inprogress:

    handle_events()

    stonegrass.draw()

    update_canvas()

import random
from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

class Mushroom:
    image = None

    def __init__(self):
        if Mushroom.image == None:
            Mushroom.image = load_image('marios.png')
        self.x = random.randint(1100, 1400)
        self.x = clamp(1300 + 25, self.x, 1600 - 25)
        self.y, self.speed = 70, 0
        self.frame = 0
        self.dir = 1
        self.speed = RUN_SPEED_PPS

    def get_bb(self):
        return self.x - 20, self.y - 20, self.x + 20, self.y + 20

    def draw(self):
        self.image.clip_draw(294 + int(self.frame) * 20, 195, 20, 22, self.x, self.y, 50, 50)
        draw_rectangle(*self.get_bb()) # 튜플을 4개의 파리미터로 나눠준다

    def update(self):
        if self.dir == 1:
            self.x += self.speed * game_framework.frame_time
        else:
            self.x -= self.speed * game_framework.frame_time

        if self.x >= 1400:
            self.dir = 0
        elif self.x <= 1100:
            self.dir = 1
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 2

    #fill here for def stop
    def stop(self):
        self.speed = 0


import game_framework
from pico2d import *
# from ball import Ball

import game_world


history = []

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 30.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

JUMP_KMPH = 40.0
JUMP_MPM = (JUMP_KMPH * 1000.0 / 60.0)
JUMP_MPS = (JUMP_MPM / 60.0)
JUMP_PPS = (JUMP_MPS * PIXEL_PER_METER)

# Boy Event
RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, z_UP, z_DOWN, DASH_TIMER, DEBUG_KEY, Jump = range(9)

event_name = ['RIGHT_DOWN', 'LEFT_DOWN', 'RIGHT_UP', 'LEFT_UP',\
'z_UP', 'z_DOWN', 'DASH_TIMER' , 'DEBUG_KEY', 'Jump']

key_event_table = {
    (SDL_KEYDOWN, SDLK_d): DEBUG_KEY,

    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): Jump,

    (SDL_KEYDOWN, SDLK_z): z_DOWN,
    (SDL_KEYUP, SDLK_z): z_UP,
}


class IdleState:

    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        if event == Jump:
            mario.jump()
        mario.timer = 1000

    def exit(mario, event):
        pass
        # if event == Jump:
        #     for jump in range(20):
        #         print('forrun')
        #         mario.jump()

    def do(mario):
        mario.timer -= 1

    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(275, 340, 15, 18, mario.x, mario.y, 60, 60)
        else:
            mario.image.clip_draw(222, 340, 15, 18, mario.x, mario.y, 60, 60)


class RunState:

    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        mario.dir = clamp(-1, mario.velocity, 1)

    def exit(mario, event):
        pass
        # if event == Jump:
        #     for jump in range(20):
        #         print('forrun')
        #         mario.jump()

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        mario.timer -= 1
        mario.x += mario.velocity * game_framework.frame_time
        mario.x = clamp(25, mario.x, 1600 - 25)

    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(290 + int(mario.frame) * 15, 340, 15, 18, mario.x, mario.y, 60, 60)
        else:
            mario.image.clip_draw(176 + int(mario.frame) * 15, 340, 15, 18, mario.x, mario.y, 60, 60)


class DashState:

    def enter(mario, event):
        print('ENTER Dash')
        mario.dir = mario.velocity

    def exit(mario, event):
        pass
        # if event == Jump:
        #     for jump in range(20):
        #         print('forrun')
        #         mario.jump()
        # print('EXIT DASH')

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        mario.x += (mario.velocity * 2) * game_framework.frame_time
        mario.x = clamp(25, mario.x, 1600 - 25)

    def draw(mario):
        if mario.dir > 1:
            mario.image.clip_draw(290 + int(mario.frame) * 15, 340, 15, 18, mario.x, mario.y, 60, 60)
        else:
            mario.image.clip_draw(176 + int(mario.frame) * 15, 340, 15, 18, mario.x, mario.y, 60, 60)

# class Jump:
#
#     def enter(mario, event):
#         print('ENTER Jump')
#         mario.dir = mario.velocity
#         mario.timer = 100
#
#     def do(mario):
#         mario.y += JUMP_PPS
#         mario.timer -= 1
#         if mario.timer == 0:
#             mario.timer = 100
#             for
#             mario.y -= JUMP_PPS
#
#
#     def draw(mario):
#         if mario.dir >= 1:
#             mario.clip_draw(352, 340, 22, 18, mario.x, mario.y, 60, 60)
#         else:
#             mario.clip_draw(140, 340, 19, 18, mario.x, mario.y, 60, 60)
#





# def fire_ball(self):
#     ball = Ball(self.x, self.y, self.dir*3)
#     game_world.add_object(ball, 1)


next_state_table = {
    DashState: {z_UP: RunState, z_DOWN: RunState, DASH_TIMER: RunState, LEFT_UP: IdleState,
                LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, RIGHT_UP: IdleState, Jump: DashState },
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState,
                z_DOWN: IdleState, z_UP: IdleState, Jump: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState,
               z_DOWN: DashState, z_UP: RunState, Jump: RunState}
}



class Mario:

    def __init__(self):
        self.x, self.y = 1600 // 2, 78
        self.image = load_image('marios.png')
        self.dir = 1
        self.velocity = 0
        self.yvelocity = 0
        self.gravity = 1
        self.jumptimer = 100
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        return self.x - 25, self.y - 30, self.x + 25, self.y + 30

    def jump(self):
        self.yvelocity += JUMP_PPS
        if self.jumptimer > 0:
            self.jumptimer -= 1
            # self.dir = self.velocity
            # self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
            self.y += (self.yvelocity * 1) * game_framework.frame_time
            self.y = clamp(78, self.y, 800 - 25)
            if self.dir >= 1:
                self.image.clip_draw(352, 340, 22, 18, self.x, self.y, 60, 60)
                print("RUN")
            else:
                self.image.clip_draw(140, 340, 19, 18, self.x, self.y, 60, 60)
                print("RUN")
        if self.jumptimer == 0:
            self.jumptimer = 100

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)

            try:
                self.cur_state = next_state_table[self.cur_state][event]
                history.append((self.cur_state.__name__, event_name[event]))
            except:
                print('State :', self.cur_state.__name__,' Event :', event_name[event])
                exit(-1)

            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        debug_print('Velocity :' + str(self.velocity) + '  Dir:' + str(self.dir))
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            if DEBUG_KEY == key_event:
                print(history[-10:])
            else:
                self.add_event(key_event)


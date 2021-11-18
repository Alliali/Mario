import random
import json
import os

from pico2d import *
import game_framework
import game_world

from mario import Mario
from maingrass import Maingrass
from background import Background
from enemy import Mushroom
from block import Broken_block
from block import Stair_block
from block import Item_block
# from ball import Ball


name = "MainState"

mario = None
maingrass = None
background = None
block = None

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global mario, maingrass, background, enemy, brokenblock, stairblock, itemblock
    mario = Mario()
    maingrass = Maingrass()
    background = Background()
    enemy = Mushroom()
    brokenblock = Broken_block()
    stairblock = Stair_block()
    itemblock = Item_block()

    game_world.add_object(maingrass, 0)
    game_world.add_object(mario, 1)
    game_world.add_object(background, 0)
    game_world.add_object(enemy, 1)
    game_world.add_object(brokenblock, 1)
    game_world.add_object(stairblock, 1)
    game_world.add_object(itemblock, 1)



def exit():
    global mario, maingrass, background, enemy, brokenblock, stairblock, itemblock
    del mario, maingrass, background, enemy, brokenblock, stairblock, itemblock
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            mario.handle_event(event)


def update():
    mario.update()
    for game_object in game_world.all_objects():
        game_object.update()
    if collide(mario, enemy):
        enemy.stop()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    background.draw()
    maingrass.draw()
    enemy.draw()
    mario.draw()
    brokenblock.draw()
    stairblock.draw()
    itemblock.draw()


    update_canvas()







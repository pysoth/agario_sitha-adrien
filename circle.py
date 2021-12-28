import random
import pygame
from pygame.math import Vector2
import core


def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [400, 400]

    core.memory("centredecercle", Vector2(100,200))
    core.memory("rayonducercle", 10)
    core.memory("couleurducercle", (255, 0, 0))

    core.memory("direction" ,Vector2(0,0))

    print("Setup END-----------")


def run():
    core.cleanScreen()
    pygame.draw.circle(core.screen, core.memory("couleurducercle"), core.memory("centredecercle"), core.memory("rayonducercle"))

    if core.getKeyPressList(pygame.K_r) :
        core.memory("direction", Vector2(0, 0))

    if core.getKeyPressList(pygame.K_z) :
        core.memory("direction", Vector2(core.memory("direction").x, -1))
    if core.getKeyPressList(pygame.K_s) :
        core.memory("direction", Vector2(core.memory("direction").x, 1))
    if core.getKeyPressList(pygame.K_q) :
        core.memory("direction", Vector2(-1,core.memory("direction").y))
    if core.getKeyPressList(pygame.K_d) :
        core.memory("direction", Vector2(1,core.memory("direction").y))

    if core.memory("centredecercle").y  < 0  or core.memory("centredecercle").y > core.WINDOW_SIZE[1] :
        core.memory("direction", Vector2(core.memory("direction").x, core.memory("direction").y*-1))
        core.memory("couleurducercle", (random.randint(0,255),random.randint(0,255), random.randint(0,255)))

    if core.memory("centredecercle").x < 0 or core.memory("centredecercle").x > core.WINDOW_SIZE[0]:
        core.memory("direction", Vector2(core.memory("direction").x*-1, core.memory("direction").y ))
        core.memory("couleurducercle", (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    core.memory("centredecercle" , core.memory("direction")+core.memory("centredecercle"))

    print(core.memory("direction").length())
core.main(setup, run)
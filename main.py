from pygame.math import Vector2
from creep import Creep
import core

import pygame

def setup():
    print("setup start....")
    core.fps = 30
    core.WINDOW_SIZE = [800,600]
    core.memory("listcreep",[])
    core.memory("nbcreep",100)


    for creep in range(0, core.memory("nbcreep")):
        core.memory("listcreep").append(creep(800,600))




    print("setup END......")


def run () :
    core.cleanScreen()
    core.printMemory()

    for creep in core.memory("listcreep"):
        creep.show(core.screen)



core.main(setup, run)
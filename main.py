from bone_farming import *
from cactus_farming import *
from companion_farming import *
from helpers import *
from maze_farming import *
from pumpkin_farming import *
from sunflower_farming import *

if can_harvest():
    harvest()
clear()
change_hat(Hats.Traffic_Cone)
do_a_flip()


def companion_core(ent_type: Entity):
    start_farm(ent_type)


def sunflower_core():
    while True:
        farm_sunflowers()


def pumpkin_core():
    while True:
        plant_pumpkins()
        make_big_pumpkin()

        harvest()


def maze_core():
    start_maze()


def cactus_core():
    while True:
        multi_cactus(False)


def snake_core():
    farm_bones()


maze_core()

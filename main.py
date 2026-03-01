import bone_farming
import cactus_farming
import companion_farming
import helpers
import maze_farming
import pumpkin_farming

if can_harvest():
    harvest()
clear()
change_hat(Hats.Traffic_Cone)
do_a_flip()


def companion_core(ent_type: Entity):
    companion_farming.start_farm(ent_type)


def pumpkin_core():
    while True:
        pumpkin_farming.plant_pumpkins()
        pumpkin_farming.make_big_pumpkin()

        harvest()


def maze_core():
    maze_farming.start_maze()


def cactus_core():
    while True:
        cactus_farming.multi_cactus()


def snake_core():
    bone_farming.farm_bones()


maze_core()

from helpers import *


def plant_pumpkin_col():
    entitiy_hat(Entities.Pumpkin)
    for _ in range(get_world_size()):
        till_grassland(Entities.Pumpkin)
        plant(Entities.Pumpkin)
        move(North)

    # Because Piggy is the best
    pet_the_piggy()


def plant_pumpkins():
    move_to(0, 0)

    for _ in range(get_world_size() - 1):
        spawn_drone(plant_pumpkin_col)
        move_to(get_pos_x() + 1, get_pos_y())

    move_to(get_world_size() - 1, 0)

    plant_pumpkin_col()


def manage_pumpkin_col():
    entitiy_hat(Entities.Pumpkin)
    while True:
        finished = True
        for _ in range(get_world_size()):
            if not can_harvest():
                till_grassland(Entities.Pumpkin)
                plant(Entities.Pumpkin)
                finished = False

            move(North)

        if finished:
            break


def make_big_pumpkin():
    move_to(0, 0)

    for _ in range(get_world_size() - 1):
        spawn_drone(manage_pumpkin_col)
        move_to(get_pos_x() + 1, get_pos_y())

    manage_pumpkin_col()

    move_to(0, 0)
    while num_drones() > 1:
        continue

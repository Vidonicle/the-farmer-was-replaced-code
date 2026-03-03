from helpers import *


def plant_sunflower_col():
    change_hat(Hats.Sunflower_Hat)
    for _ in range(get_world_size()):
        till_grassland()
        plant(Entities.Sunflower)
        use_water(4)

        move(North)

    # Because Piggy is the best
    pet_the_piggy()


def plant_sunflower():
    move_to(0, 0)

    for _ in range(get_world_size() - 1):
        spawn_drone(plant_sunflower_col)
        move_to(get_pos_x() + 1, get_pos_y())

    plant_sunflower_col()


def farm_sunflower_col(max_petals):
    change_hat(Hats.Sunflower_Hat)
    for _ in range(get_world_size()):
        petals = measure()
        if petals == max_petals:
            while not can_harvest():
                continue
            harvest()
        move(North)


def farm_size():
    farm_sunflower_col(current_size)


def farm_sunflowers():

    move_to(0, 0)
    plant_sunflower()
    global current_size

    move_to(0, 0)

    for x in range(15, 6, -1):
        current_size = x
        for _ in range(get_world_size() - 1):
            spawn_drone(farm_size)
            move_to(get_pos_x() + 1, get_pos_y())

        farm_size()

        while num_drones() > 1:
            continue

        move_to(0, 0)

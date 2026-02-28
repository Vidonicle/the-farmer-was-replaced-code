import create_farms
import focus_farms
import helpers
import maze
import start_farms

if can_harvest():
    harvest()
clear()
change_hat(Hats.Traffic_Cone)
do_a_flip()


def farm_core():
    create_farms.init_plant()
    start_farms.farm()


def hay_core():
    # Because Piggy is the best
    pet_the_piggy()

    start_farms.companion_farm(Entities.Grass)


def carrot_core():
    start_farms.companion_farm(Entities.Carrot)


def wood_core():
    start_farms.companion_farm(Entities.Tree)


def sunflower_core():
    create_farms.plant_sunflower()
    while True:
        start_farms.farm_sunflower()


def pumpkin_core():
    while True:
        create_farms.plant_pumpkin()
        start_farms.farm_pumpkin()


def maze_core():
    while True:
        maze.create_maze()
        if num_drones() < 2:
            spawn_drone(maze.search_left)
        maze.search_right()


def cactus_core():
    while True:
        create_farms.plant_cactus()
        start_farms.sort_columns()
        start_farms.sort_rows()
        harvest()


def snake_core():
    while True:
        start_farms.farm_bones()
        change_hat(Hats.Traffic_Cone)


def focus_drones_core():
    create_farms.init_plant()
    spawn_drone(focus_farms.focus_hay)
    spawn_drone(focus_farms.focus_bush)
    spawn_drone(focus_farms.focus_carrot)
    spawn_drone(focus_farms.focus_tree)
    focus_farms.focus_pumpkins()


maze_core()

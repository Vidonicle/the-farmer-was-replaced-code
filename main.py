import create_farms
import maze
import start_farms

clear()
change_hat(Hats.Traffic_Cone)
do_a_flip()


def maze_core():
    while True:
        maze.create_maze()
        if num_drones() < 2:
            spawn_drone(maze.search_left)
        maze.search_right()


def farm_core():
    create_farms.init_plant()
    start_farms.farm()


def cactus_core():
    while True:
        create_farms.plant_cactus()
        start_farms.sort_columns()
        start_farms.sort_rows()
        harvest()


def sunflower_core():
    create_farms.plant_sunflower()
    while True:
        start_farms.farm_sunflower()


cactus_core()

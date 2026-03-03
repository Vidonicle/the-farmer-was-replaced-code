from helpers import *


def plant_cactus_col():
    entitiy_hat(Entities.Cactus)
    for _ in range(get_world_size()):
        till_grassland(Entities.Cactus)
        plant(Entities.Cactus)
        move(North)


def bubble_col():
    entitiy_hat(Entities.Cactus)
    for _ in range(get_world_size()):
        # Used to check if we can stop early to save time and energy
        col_sorted = True

        # For each pass of a column
        for _ in range(get_world_size() - 1):
            curr_size = measure()
            next_size = measure(North)

            if curr_size > next_size:
                col_sorted = False
                swap(North)
            move(North)

        move(North)

        if col_sorted:
            break


def bubble_row():
    entitiy_hat(Entities.Cactus)
    for _ in range(get_world_size()):
        # Used to check if we can stop early to save time and energy
        row_sorted = True

        # For each pass of a row
        for _ in range(get_world_size() - 1):
            curr_size = measure()
            next_size = measure(East)

            if curr_size > next_size:
                row_sorted = False
                swap(East)
            move(East)

        move(East)

        if row_sorted:
            break


def insertion_col():
    entitiy_hat(Entities.Cactus)
    move(North)

    for i in range(1, get_world_size()):
        curr = measure()
        prev = measure(South)

        while get_pos_y() > 0 and prev > curr:
            swap(South)
            move(South)
            curr = measure()
            prev = measure(South)

        move_to(get_pos_x(), i + 1)


def insertion_row():
    entitiy_hat(Entities.Cactus)
    move(East)

    for i in range(1, get_world_size()):
        curr = measure()
        prev = measure(West)

        while get_pos_x() > 0 and prev > curr:
            swap(West)
            move(West)
            curr = measure()
            prev = measure(West)

        move_to(i + 1, get_pos_y())


def multi_cactus(bubble=True):
    if bubble:
        col_sort = bubble_col
        row_sort = bubble_row
    else:
        col_sort = insertion_col
        row_sort = insertion_row

    move_to(0, 0)

    for _ in range(get_world_size() - 1):
        spawn_drone(plant_cactus_col)
        move_to(get_pos_x() + 1, get_pos_y())

    plant_cactus_col()

    move_to(0, 0)

    for _ in range(get_world_size() - 1):
        spawn_drone(col_sort)
        move_to(get_pos_x() + 1, get_pos_y())

    col_sort()

    move_to(0, 0)

    while num_drones() > 1:
        continue

    for _ in range(get_world_size() - 1):
        spawn_drone(row_sort)
        move_to(get_pos_x(), get_pos_y() + 1)

    row_sort()
    move_to(0, 0)

    while num_drones() > 1:
        continue

    harvest()

from helpers import *

dirs = [North, East, South, West]
substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)


def create_maze():
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, substance)


def try_move(dir_idx):
    if can_move(dirs[dir_idx]):
        move(dirs[dir_idx])
        return True
    return False


def search_wall(favour_right=True, sentinel=False):
    while True:

        while get_entity_type() != Entities.Hedge:
            if sentinel:
                create_maze()
            else:
                pass

        index = 0
        while True:
            if get_entity_type() == Entities.Treasure:
                harvest()
            if get_entity_type() != Entities.Hedge:
                break

            right = (index + 1) % 4
            forward = index
            left = (index - 1) % 4
            back = (index + 2) % 4

            if favour_right:
                if try_move(right):
                    index = right
                elif try_move(forward):
                    pass
                elif try_move(left):
                    index = left
                else:
                    try_move(back)
                    index = back
            else:
                if try_move(left):
                    index = left
                elif try_move(forward):
                    pass
                elif try_move(right):
                    index = right
                else:
                    try_move(back)
                    index = back


def search_right():
    change_hat(Hats.The_Farmers_Remains)
    search_wall(True)


def search_left():
    change_hat(Hats.The_Farmers_Remains)
    search_wall(False)


def start_maze():
    move_to(1, 1)

    for i in range(max_drones() - 1):
        if i % 2 == 0:
            spawn_drone(search_right)
        else:
            spawn_drone(search_left)

        move_to(get_pos_x() + 1, get_pos_y() + 1)

    move_to(0, 0)
    # Because Piggy is the best
    pet_the_piggy()
    search_wall(False, True)

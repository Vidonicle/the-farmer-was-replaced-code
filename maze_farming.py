import helpers

dirs = [North, East, South, West]
substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)


def create_maze():
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, substance)

    # Because Piggy is the best
    pet_the_piggy()


def try_move(dir_idx):
    if can_move(dirs[dir_idx]):
        move(dirs[dir_idx])
        return True
    return False


def search_wall(favour_right=True, sentinel=False):
    while True:
        while get_entity_type() != Entities.Hedge:
            helpers.do_nothing()
            if sentinel:
                create_maze()

        index = 0
        while True:
            if get_entity_type() == Entities.Treasure:
                harvest()
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


def sentinel():
    search_wall(False, True)


def start_maze():
    helpers.move_to(0, 0)

    for i in range(max_drones() // 4):
        if i % 2 == 0:
            spawn_drone(search_right)
        else:
            spawn_drone(search_left)

        if i == 0:
            helpers.move_to(get_pos_x() + 3, get_pos_y())

        else:
            helpers.move_to(get_pos_x() + 4, get_pos_y())

    for i in range(max_drones() // 4):
        if i % 2 == 0:
            spawn_drone(search_left)
        else:
            spawn_drone(search_right)

        if i == 0:
            helpers.move_to(get_pos_x(), get_pos_y() + 3)
        else:
            helpers.move_to(get_pos_x(), get_pos_y() + 4)

    for i in range(max_drones() // 4):
        if i % 2 == 0:
            spawn_drone(search_right)
        else:
            spawn_drone(search_left)

        if i == 0:
            helpers.move_to(get_pos_x() - 3, get_pos_y())
        else:
            helpers.move_to(get_pos_x() - 4, get_pos_y())

    for i in range(max_drones() // 4 - 1):
        if i % 2 == 0:
            spawn_drone(search_left)
        else:
            spawn_drone(search_right)

        if i == 0:
            helpers.move_to(get_pos_x(), get_pos_y() - 3)
        else:
            helpers.move_to(get_pos_x(), get_pos_y() - 4)

    sentinel()

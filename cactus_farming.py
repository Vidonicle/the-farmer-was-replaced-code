import helpers


def plant_cactus_col():
    helpers.entitiy_hat(Entities.Cactus)
    for _ in range(get_world_size()):
        helpers.till_grassland(Entities.Cactus)
        plant(Entities.Cactus)
        move(North)


def sort_one_col():
    helpers.entitiy_hat(Entities.Cactus)
    (homex, homey) = helpers.get_position()
    for _ in range(get_world_size()):
        # Used to check if we can stop early to save time and energy
        col_sorted = True

        # For each pass of a column
        for _ in range(get_world_size()):
            current_size = measure()
            north_size = measure(North)

            if current_size > north_size and get_pos_y() != get_world_size() - 1:
                col_sorted = False
                swap(North)
            move(North)

        if col_sorted:
            break


def sort_one_row():
    helpers.entitiy_hat(Entities.Cactus)
    for _ in range(get_world_size()):
        # Used to check if we can stop early to save time and energy
        row_sorted = True

        # For each pass of a row
        for _ in range(get_world_size()):
            current_size = measure()
            east_size = measure(East)

            if current_size > east_size and get_pos_x() != get_world_size() - 1:
                row_sorted = False
                swap(East)
            move(East)

        if row_sorted:
            break


def multi_cactus():
    helpers.move_to(0, 0)

    for _ in range(max_drones() - 1):
        spawn_drone(plant_cactus_col)
        helpers.move_to(get_pos_x() + 1, get_pos_y())

    plant_cactus_col()

    helpers.move_to(0, 0)

    for _ in range(max_drones() - 1):
        spawn_drone(sort_one_col)
        helpers.move_to(get_pos_x() + 1, get_pos_y())

    sort_one_col()

    helpers.move_to(0, 0)

    while num_drones() > 1:
        helpers.do_nothing()

    for _ in range(max_drones() - 1):
        spawn_drone(sort_one_row)
        helpers.move_to(get_pos_x(), get_pos_y() + 1)

    sort_one_row()
    helpers.move_to(0, 0)

    while num_drones() > 1:
        helpers.do_nothing()

    harvest()

import helpers


def plant_pumpkin_col():
    helpers.entitiy_hat(Entities.Pumpkin)
    for _ in range(get_world_size()):
        helpers.till_grassland(Entities.Pumpkin)
        plant(Entities.Pumpkin)
        move(North)

    # Because Piggy is the best
    pet_the_piggy()


def plant_pumpkins():
    helpers.move_to(0, 0)

    for _ in range(max_drones() - 1):
        spawn_drone(plant_pumpkin_col)
        helpers.move_to(get_pos_x() + 1, get_pos_y())

    helpers.move_to(get_world_size() - 1, 0)

    plant_pumpkin_col()


def manage_pumpkin_col():
    helpers.entitiy_hat(Entities.Pumpkin)
    while True:
        finished = True
        for _ in range(get_world_size()):
            if not can_harvest():
                helpers.till_grassland(Entities.Pumpkin)
                plant(Entities.Pumpkin)
                finished = False

            move(North)

        if finished:
            break


def make_big_pumpkin():
    helpers.move_to(0, 0)

    for _ in range(max_drones() - 1):
        spawn_drone(manage_pumpkin_col)
        helpers.move_to(get_pos_x() + 1, get_pos_y())

    helpers.move_to(get_world_size() - 1, 0)

    manage_pumpkin_col()

    helpers.move_to(0, 0)
    while num_drones() > 1:
        helpers.do_nothing()

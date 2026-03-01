import helpers


def companion_farm():
    (originx, originy) = helpers.get_position()

    origin_ent = get_entity_type()
    helpers.entitiy_hat(origin_ent)

    while True:
        companion, (x, y) = get_companion()

        helpers.move_to(x, y)

        if get_entity_type() != companion:
            harvest()
            helpers.till_grassland(companion)
            plant(companion)

        helpers.move_to(originx, originy)

        while not can_harvest():
            helpers.use_water(1, 0.95)
            continue

        harvest()
        helpers.till_grassland(origin_ent)
        plant(origin_ent)


def start_farm(ent_type: Entity):
    set_world_size(28)

    helpers.move_to(3, 3)

    for y in range(4):
        for x in range(4):
            helpers.till_grassland(ent_type)
            plant(ent_type)
            spawn_drone(companion_farm)
            helpers.move_to(get_pos_x() + 7, get_pos_y())

        helpers.move_to(get_pos_x(), get_pos_y() + 7)

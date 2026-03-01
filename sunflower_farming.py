import helpers


def plant_sunflower():
    set_world_size(4)

    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            helpers.till_grassland()
            plant(Entities.Sunflower)
            helpers.use_water(2, 0.50)

            move(North)
        move(East)

    # Because Piggy is the best
    pet_the_piggy()


def farm_sunflower():
    helpers.entitiy_hat(Entities.Sunflower)
    largest_sunflower = 0
    largestpos = (0, 0)

    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            petals = measure()

            if petals >= largest_sunflower:
                if petals == 15 and can_harvest():
                    harvest()
                    helpers.till_grassland()
                    plant(Entities.Sunflower)
                    helpers.use_water(4)
                else:
                    largest_sunflower = petals
                    largestpos = helpers.get_position()

            move(North)
        move(East)

    helpers.move_to(largestpos[0], largestpos[1])

    while not can_harvest():
        helpers.use_water(1, 0.95)
        continue

    if can_harvest():
        harvest()
        helpers.till_grassland()
        plant(Entities.Sunflower)

import helpers

pumpkin_tiles = helpers.get_pumpkin_tiles(12)


# Starter farming ------
def farm():
    while True:
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                pos = helpers.get_position()
                ent_type = get_entity_type()

                if can_harvest():
                    harvest()

                helpers.till_grassland(ent_type)

                if pos in pumpkin_tiles:
                    plant(Entities.Pumpkin)
                else:
                    plant(ent_type)
                    if ent_type == Entities.Tree:
                        use_item(Items.Fertilizer)

                helpers.use_water()

                move(North)
            move(North)
            move(East)


# ----------------------


# Companion farming ----
def companion_farm(ent_type: Entity, originx=0, originy=0):

    while get_pos_x() != originx:
        move(West)
    while get_pos_y() != originy:
        move(South)

    helpers.till_grassland(ent_type)
    plant(ent_type)

    set_world_size(4)

    while True:
        companion, (x, y) = get_companion()

        quick_print(companion, (x, y))

        dx = x - get_pos_x()
        if dx > 0:
            for _ in range(dx):
                move(East)
            homex = West
        elif dx < 0:
            for _ in range(dx):
                move(West)
            homex = East

        dy = y - get_pos_y()
        if dy > 0:
            for _ in range(dy):
                move(North)
            homey = South
        elif dy < 0:
            for _ in range(dy):
                move(South)
            homey = North

        harvest()
        helpers.till_grassland(companion)
        plant(companion)

        while get_pos_x() != originx:
            move(homex)
        while get_pos_y() != originy:
            move(homey)

        while not can_harvest():
            helpers.use_water(1, 1.00)
            continue

        harvest()
        helpers.till_grassland(ent_type)
        plant(ent_type)


# ----------------------


# # Carrot farming -------
# def farm_carrot():
#     for _ in range(get_world_size()):
#         for _ in range(get_world_size()):
#             if can_harvest():
#                 harvest()
#                 helpers.till_grassland()
#                 plant(Entities.Carrot)
#                 helpers.use_water(1, 0.5)

#             move(North)

#         move(East)


# # ----------------------


# # Tree farming ---------
# def farm_wood():
#     for _ in range(get_world_size()):
#         for _ in range(get_world_size()):
#             ent_type = get_entity_type()

#             if can_harvest():
#                 harvest()

#             plant(ent_type)
#             if ent_type == Entities.Tree:
#                 helpers.use_water()

#             move(North)

#         move(North)
#         move(East)


# # ----------------------


# Sunflower farming ----
def farm_sunflower():

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

    while get_pos_x() != largestpos[0]:
        move(East)
    while get_pos_y() != largestpos[1]:
        move(North)

    while not can_harvest():
        helpers.use_water(1, 0.95)
        continue

    if can_harvest():
        harvest()
        helpers.till_grassland()
        plant(Entities.Sunflower)


# ----------------------


# Pumpkin farming ------
def farm_pumpkin():
    while True:
        full_size = True
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):

                if can_harvest() == False:
                    full_size = False
                    plant(Entities.Pumpkin)

                move(North)

            move(East)

        if full_size == True:
            break

    while get_pos_x() != 0:
        move(East)
    while get_pos_y() != 0:
        move(North)

    harvest()


# ----------------------


# Cactus farming ---
def sort_columns():
    # Uses a bubble sort algorithm O(n^3)
    # For all columns on the plot
    for _ in range(get_world_size()):

        # For all tiles on the column
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

        move(East)


def sort_rows():
    # Uses a bubble sort algorithm O(n^3)
    # For all rows on the plot
    for _ in range(get_world_size()):

        # For all tiles on the row
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

        move(North)


# ----------------------


def farm_bones():
    change_hat(Hats.Dinosaur_Hat)
    while True:
        for _ in range(get_world_size() - 1):
            if not move(North):
                return

        move(East)

        for _ in range(get_world_size() // 2):
            for _ in range(get_world_size() - 2):
                move(South)

            move(East)

            for _ in range(get_world_size() - 2):
                move(North)

            move(East)

        move(South)
        for _ in range(get_world_size()):
            move(West)

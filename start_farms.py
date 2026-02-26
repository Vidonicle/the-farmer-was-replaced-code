import helpers

side_length = get_world_size()

# Basic farming --------
pumpkin_tiles = set()

edge_coords_pumpkins = (
    side_length - 5,
    side_length - 4,
    side_length - 3,
    side_length - 2,
    side_length - 1,
)

dont_water = [Entities.Grass, Entities.Pumpkin]

for x in range(side_length):
    for y in edge_coords_pumpkins:
        pumpkin_tiles.add((x, y))

for x in edge_coords_pumpkins:
    for y in range(side_length):
        pumpkin_tiles.add((x, y))


def farm():
    while True:
        for _ in range(side_length):
            for _ in range(side_length):
                pos = helpers.get_position()
                gnd_type = get_ground_type()
                ent_type = get_entity_type()

                if can_harvest():
                    harvest()

                if pos in pumpkin_tiles:
                    helpers.till_grassland()
                    plant(Entities.Pumpkin)
                else:
                    plant(ent_type)
                    if ent_type == Entities.Tree:
                        use_item(Items.Fertilizer)

                if ent_type not in dont_water:
                    helpers.use_water()

                move(North)
            move(North)
            move(East)
# ----------------------


# Cactus farming ---
def sort_columns():
    # Uses a bubble sort algorithm O(n^3)
    # For all columns on the plot
    for _ in range(side_length):

        # For all tiles on the column
        for _ in range(side_length):
            # Used to check if we can stop early to save time and energy
            col_sorted = True

            # For each pass of a column
            for _ in range(side_length):
                current_size = measure()
                north_size = measure(North)

                if current_size > north_size and get_pos_y() != side_length - 1:
                    col_sorted = False
                    swap(North)
                move(North)

            if col_sorted:
                break

        move(East)


def sort_rows():
    # Uses a bubble sort algorithm O(n^3)
    # For all rows on the plot
    for _ in range(side_length):

        # For all tiles on the row
        for _ in range(side_length):
            # Used to check if we can stop early to save time and energy
            row_sorted = True

            # For each pass of a row
            for _ in range(side_length):
                current_size = measure()
                east_size = measure(East)

                if current_size > east_size and get_pos_x() != side_length - 1:
                    row_sorted = False
                    swap(East)
                move(East)

            if row_sorted:
                break

        move(North)
# ----------------------

# Sunflower farming ----
def farm_sunflower():
    side_length = get_world_size()

    largest_sunflower = 0
    largestpos = (0, 0)

    for _ in range(side_length):
        for _ in range(side_length):
            petals = measure()

            if petals >= largest_sunflower:
                if petals == 15 and can_harvest():
                    harvest()
                    helpers.till_grassland()
                    plant(Entities.Sunflower)
                    helpers.use_water(3)
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
        continue

    if can_harvest():
        harvest()
        helpers.till_grassland()
        plant(Entities.Sunflower)
        helpers.use_water(3)
        helpers.use_water(3)
# ----------------------

# Tree farming ---------
def farm_wood():
    for _ in range(side_length):
        for _ in range(side_length):
            ent_type = get_entity_type()

            if can_harvest():
                harvest()

            plant(ent_type)
            if ent_type == Entities.Tree:
                helpers.use_water()
            
            move(North)
        
        move(North)
        move(East)
# ----------------------
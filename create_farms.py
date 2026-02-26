import helpers

dirs = [North, East, South, West]
dont_water = [Entities.Grass, Entities.Pumpkin]

side_length = get_world_size()

pumpkin_tiles = set()

edge_coords_pumpkins = (
    side_length - 5,
    side_length - 4,
    side_length - 3,
    side_length - 2,
    side_length - 1,
)

for x in range(side_length):
    for y in edge_coords_pumpkins:
        pumpkin_tiles.add((x, y))

for x in edge_coords_pumpkins:
    for y in range(side_length):
        pumpkin_tiles.add((x, y))


def init_plant():
    for _ in range(side_length):
        for j in range(side_length):
            pos = helpers.get_position()
            k = j % 4

            if pos in pumpkin_tiles:
                helpers.till_grassland()
                plant(Entities.Pumpkin)
            else:
                if k == 0:
                    # Grass
                    pass
                elif k == 1:
                    # Bush / Tree
                    plant(Entities.Tree)
                elif k == 2:
                    # Carrot
                    helpers.till_grassland()
                    plant(Entities.Carrot)
                elif k == 3:
                    # Sunflower
                    helpers.till_grassland()
                    plant(Entities.Sunflower)

                if get_entity_type() not in dont_water:
                    helpers.use_water()

            move(North)
        move(North)
        move(East)
    pet_the_piggy()


def plant_cactus():
    for _ in range(side_length):
        for _ in range(side_length):
            helpers.till_grassland()
            plant(Entities.Cactus)
            move(North)
        move(East)


def plant_sunflower():
    set_world_size(4)
    side_length = get_world_size()

    for _ in range(side_length):
        for _ in range(side_length):
            helpers.till_grassland()
            plant(Entities.Sunflower)
            helpers.use_water(2, 0.51)

            move(North)
        move(East)

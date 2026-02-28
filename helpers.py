tilled_plants = {Entities.Carrot, Entities.Sunflower, Entities.Pumpkin, Entities.Cactus}


def get_tile_group(start, end):
    tile_group = ()
    for i in range(end - start, end):
        tile_group = tile_group + (i,)

    return tile_group


def till_grassland(ent_type=None):
    if ent_type in tilled_plants or ent_type == None:
        if get_ground_type() != Grounds.Soil:
            till()


def get_position() -> tuple[int, int]:
    return (get_pos_x(), get_pos_y())


def use_water(times=1, threshold=0.75):
    # Water use doesn't need to be greater than 4
    if times > 4:
        times = 4

    # Minimum use 1
    if times < 1:
        times = 1

    if threshold < 0.00:
        threshold = 0.01

    if threshold > 1:
        threshold = 0.75

    if get_water() <= threshold:
        use_item(Items.Water, times)


def get_pumpkin_tiles(n):
    pumpkin_tiles = set()

    edge_coords_pumpkins = get_tile_group(n, get_world_size())

    for x in range(get_world_size()):
        for y in edge_coords_pumpkins:
            pumpkin_tiles.add((x, y))

    for x in edge_coords_pumpkins:
        for y in range(get_world_size()):
            pumpkin_tiles.add((x, y))

    return pumpkin_tiles

def till_grassland():
    if get_ground_type() != Grounds.Soil:
        till()


def get_position() -> tuple[int, int]:
    return (get_pos_x(), get_pos_y())


def use_water(times=1, threshold=0.25):
    # Water use doesn't need to be greater than 4
    if times > 4:
        times = 4

    # Minimum use 1
    if times < 1:
        times = 1

    if get_water() < threshold:
        uses = 0
        while uses < times:
            use_item(Items.Water)
            uses += 1

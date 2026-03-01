import helpers

pumpkin_tiles = helpers.get_pumpkin_tiles(12)


# Basic farm pattern ---
def init_plant():
    for _ in range(get_world_size()):
        for j in range(get_world_size()):
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
                    # Tree
                    plant(Entities.Tree)
                elif k == 2:
                    # Carrot
                    helpers.till_grassland()
                    plant(Entities.Carrot)
                elif k == 3:
                    # Bush
                    plant(Entities.Bush)

                helpers.use_water()

            move(North)

        move(North)
        move(East)

    # Because Piggy is the best
    pet_the_piggy()


# ----------------------


# # Carrot farm ----------
# def plant_carrot():
#     for _ in range(get_world_size()):
#         for _ in range(get_world_size()):
#             helpers.till_grassland()
#             plant(Entities.Carrot)
#             helpers.use_water(1, 0.5)

#             move(North)

#         move(East)

#     # Because Piggy is the best
#     pet_the_piggy()


# # ----------------------


# # Wood farm ------------
# def plant_wood():
#     for _ in range(get_world_size()):
#         i = 0
#         for _ in range(get_world_size()):
#             if i % 2 == 0:
#                 plant(Entities.Tree)
#                 helpers.use_water()
#             else:
#                 plant(Entities.Bush)

#             i += 1
#             move(North)

#         move(North)
#         move(East)

#     # Because Piggy is the best
#     pet_the_piggy()


# # ----------------------


# Sunflower farm -------
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


# ----------------------


# Pumpkin farm ---------
def plant_pumpkin():
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            helpers.till_grassland()
            plant(Entities.Pumpkin)
            move(North)
        move(East)

    # Because Piggy is the best
    pet_the_piggy()


# ----------------------


# Cactus farm ----------
def plant_cactus():
    for _ in range(get_world_size()):
        for _ in range(get_world_size()):
            helpers.till_grassland()
            plant(Entities.Cactus)
            move(North)
        move(East)

    # Because Piggy is the best
    pet_the_piggy()


# ----------------------

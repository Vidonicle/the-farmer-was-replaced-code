import helpers

pumpkin_tiles = helpers.get_pumpkin_tiles(12)


def focus_hay():
    while True:
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                pos = helpers.get_position()

                if pos in pumpkin_tiles:
                    move(North)
                    continue

                ent_type = get_entity_type()

                if ent_type == Entities.Grass:
                    if can_harvest():
                        harvest()

                move(North)
            move(East)


def focus_bush():
    while True:
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                pos = helpers.get_position()

                if pos in pumpkin_tiles:
                    move(North)
                    continue

                ent_type = get_entity_type()

                if ent_type == Entities.Bush:
                    if can_harvest():
                        harvest()
                    plant(Entities.Bush)

                move(North)
            move(East)


def focus_carrot():
    while True:
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                pos = helpers.get_position()

                if pos in pumpkin_tiles:
                    move(North)
                    continue

                ent_type = get_entity_type()

                if ent_type == Entities.Carrot:
                    if can_harvest():
                        harvest()
                    helpers.till_grassland()
                    plant(Entities.Carrot)

                move(North)
            move(East)


def focus_tree():
    while True:
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                pos = helpers.get_position()

                if pos in pumpkin_tiles:
                    move(North)
                    continue

                ent_type = get_entity_type()

                if ent_type == Entities.Tree:
                    if can_harvest():
                        harvest()
                    plant(Entities.Tree)

                move(North)
            move(East)


def focus_sunflower():
    while True:
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                pos = helpers.get_position()

                if pos in pumpkin_tiles:
                    move(North)
                    continue

                ent_type = get_entity_type()

                if ent_type == Entities.Sunflower:
                    if can_harvest():
                        harvest()
                    plant(Entities.Sunflower)

                move(North)
            move(East)


def focus_cactus():
    while True:
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                pos = helpers.get_position()

                if pos in pumpkin_tiles:
                    move(North)
                    continue

                ent_type = get_entity_type()

                if ent_type == Entities.Cactus:
                    if can_harvest():
                        harvest()
                    plant(Entities.Cactus)

                move(North)
            move(East)


def focus_pumpkins():
    while True:
        for _ in range(get_world_size()):
            for _ in range(get_world_size()):
                pos = helpers.get_position()

                if pos not in pumpkin_tiles:
                    move(North)
                    continue

                ent_type = get_entity_type()

                if ent_type == Entities.Pumpkin:
                    if can_harvest():
                        harvest()

                plant(Entities.Pumpkin)

                move(North)
            move(East)

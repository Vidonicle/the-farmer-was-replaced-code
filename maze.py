dirs = [North, East, South, West]
substance = get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)


def create_maze():
    plant(Entities.Bush)
    use_item(Items.Weird_Substance, substance)

    # Because Piggy is the best
    pet_the_piggy()


def try_move(dir_idx):
    if can_move(dirs[dir_idx]):
        move(dirs[dir_idx])
        return True
    return False


def search_right():
    index = 0

    while True:
        treasurex, treasurey = measure()
        quick_print((treasurex, treasurey))

        if get_entity_type() == Entities.Treasure:
            use_item(Items.Weird_Substance, substance)

        right = (index + 1) % 4
        forward = index
        left = (index - 1) % 4
        back = (index + 2) % 4

        if try_move(right):
            index = right
        elif try_move(forward):
            pass
        elif try_move(left):
            index = left
        else:
            try_move(back)
            index = back


def search_left():
    index = 0

    while True:
        treasurex, treasurey = measure()
        quick_print((treasurex, treasurey))

        if get_entity_type() == Entities.Treasure:
            use_item(Items.Weird_Substance, substance)

        right = (index + 1) % 4
        forward = index
        left = (index - 1) % 4
        back = (index + 2) % 4

        if try_move(left):
            index = left
        elif try_move(forward):
            pass
        elif try_move(right):
            index = right
        else:
            try_move(back)
            index = back

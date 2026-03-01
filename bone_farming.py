def farm_bones():
    while True:
        change_hat(Hats.Dinosaur_Hat)
        break_loop = False
        while True:
            for _ in range(get_world_size() - 1):
                if not move(North):
                    break_loop = True
                    break

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

            if break_loop:
                break

        change_hat(Hats.Traffic_Cone)
        change_hat(Hats.Dinosaur_Hat)
        while move(South):
            pass
        while move(West):
            pass

def print_map(*, player, bombs):
    line = "-" * 80
    pv_line = " " * 80
    if bombs:
        for bomb in bombs:
            line[bomb.position_x] = "o"
    if player:
        line[player.position_x] = "P"
        pv_line[player.position_x] = player.life
    print("\n" * 50)
    print(pv_line)
    print(line)

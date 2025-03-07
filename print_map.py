def print_map(*, player=None, bombs=None):
    line = ["-"] * 80
    pv_line = [" "] * 80
    if bombs:
        for bomb in bombs:
            line[bomb.position_x] = "o"
    if player:
        line[player.position_x] = "P"
        pv_line[player.position_x] = str(player.life)
    print("\n" * 50)
    print("".join(pv_line))
    print("".join(line))

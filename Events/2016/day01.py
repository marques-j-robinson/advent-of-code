from format_data import list_of_tuples
from shape import Grid
from calc import manhattan_distance


directions = {
    "up": "N",
    "right": "E",
    "down": "S",
    "left": "W"
}
turns = {
    "NR": "E",
    "NL": "W",
    "SR": "W",
    "SL": "E",
    "ER": "S",
    "EL": "N",
    "WR": "N",
    "WL": "S"
}


def p1(puzzle_input):
    puzzle_input = list_of_tuples(puzzle_input)
    d = directions["up"]
    G = Grid(directions)
    for turn, steps in puzzle_input:
        d = turns[f'{d}{turn}']
        while steps > 0:
            steps -= 1
            G.move_auto(d)
    return manhattan_distance(G.x, G.y)


def p2(puzzle_input):
    res = 0
    puzzle_input = list_of_tuples(puzzle_input)
    d = directions["up"]
    G = Grid(directions)
    for turn, steps in puzzle_input:
        d = turns[f"{d}{turn}"]
        while steps > 0:
            steps -= 1
            G.move(d)
            if res == 0 and G.coord in G.seen:
                res = manhattan_distance(G.x, G.y)
            G.add_seen()
    return res
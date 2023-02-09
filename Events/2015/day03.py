from format_data import combine
from calc import is_even
from shape import Grid


directions = {
    "up": "^",
    "right": ">",
    "down": "v",
    "left": "<"
}


def p1(puzzle_input):
    G = Grid(directions)
    G.add_seen()
    for d in puzzle_input:
        G.move_auto(d)
    return len(G.seen)


def p2(puzzle_input):
    santa = Grid(directions)
    robo_santa = Grid(directions)
    for idx, d in enumerate(puzzle_input):
        if is_even(idx):
            santa.move_auto(d)
        else:
            robo_santa.move_auto(d)
    return combine(santa.seen, robo_santa.seen)
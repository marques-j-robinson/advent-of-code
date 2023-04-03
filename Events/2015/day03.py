from main import CacheLayer, Grid


def is_even(i):
    return i % 2 == 0


def combine(a, b):
    return len(a + list(set(b) - set(a)))
        

directions = ["^", "v", "<", ">"]
p1_santa = Grid(directions)
p2_santa = Grid(directions)
robo_santa = Grid(directions)


class S(CacheLayer):

    def solve(self):
        for idx, direction in enumerate(self.puzzle_input):
            if is_even(idx):
                p2_santa.save_move(direction)
            else:
                robo_santa.save_move(direction)
            p1_santa.save_move(direction)
        self.p1 = len(p1_santa.seen)
        self.p2 = combine(p2_santa.seen, robo_santa.seen)
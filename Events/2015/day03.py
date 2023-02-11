from Events.solution import Solution
from util import Grid, is_even, combine
        

directions = ["^", "v", "<", ">"]


class S(Solution):

    def solve(self):
        p1_santa = Grid(directions)
        p2_santa = Grid(directions)
        robo_santa = Grid(directions)
        for idx, direction in enumerate(self.data):
            if is_even(idx):
                p2_santa.save_move(direction)
            else:
                robo_santa.save_move(direction)
            p1_santa.save_move(direction)
        self.p1 = len(p1_santa.seen)
        self.p2 = combine(p2_santa.seen, robo_santa.seen)

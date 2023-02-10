from Events.solution import Solution
from util import is_even, combine


up = "^"
right = ">"
down = "v"
left = "<"


class Santa:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.seen = []
        self.add_seen() # Add origin to seen list

    def move(self, d):
        if d == up:
            self.y += 1
        elif d == right:
            self.x += 1
        elif d == down:
            self.y -= 1
        elif d == left:
            self.x -= 1
        self.add_seen()

    def add_seen(self):
        coord = f"{self.x},{self.y}"
        if coord not in self.seen:
            self.seen.append(coord)


class S(Solution):

    def solve(self):
        p1_santa = Santa()
        p2_santa = Santa()
        robo_santa = Santa()
        for idx, direction in enumerate(self.data):
            if is_even(idx):
                p2_santa.move(direction)
            else:
                robo_santa.move(direction)
            p1_santa.move(direction)
        self.p1 = len(p1_santa.seen)
        self.p2 = combine(p2_santa.seen, robo_santa.seen)

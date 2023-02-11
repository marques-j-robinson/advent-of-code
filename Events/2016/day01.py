from Events.solution import Solution
from util import manhattan_distance


up = "N"
right = "E"
down = "S"
left = "W"
pivot = {
    "NR": "E",
    "NL": "W",
    "SR": "W",
    "SL": "E",
    "ER": "S",
    "EL": "N",
    "WR": "N",
    "WL": "S"
}


class Grid:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.seen = []

    def move(self, d):
        if d == up:
            self.y += 1
        elif d == right:
            self.x += 1
        elif d == down:
            self.y -= 1
        elif d == left:
            self.x -= 1

    def add_seen(self):
        coord = self.coord()
        if coord not in self.seen:
            self.seen.append(coord)

    def coord(self):
        return f"{self.x},{self.y}"


class S(Solution):

    def split_by_comma(self):
        self.data = self.data.split(', ')

    def list_of_tuples(self):
        self.data = [(d[0], int(d[1:len(d)])) for d in self.data]

    def solve(self):
        self.split_by_comma()
        self.list_of_tuples()
        direction = up
        G = Grid()
        for turn, steps in self.data:
            direction = pivot[f'{direction}{turn}']
            while steps > 0:
                G.move(direction)
                if self.p2 == 0 and G.coord() in G.seen:
                    self.p2 = manhattan_distance(G.x, G.y)
                G.add_seen()
                steps -= 1
        self.p1 = manhattan_distance(G.x, G.y)

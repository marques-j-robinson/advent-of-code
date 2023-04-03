from main import CacheLayer, int_list


class Grid:

    def __init__(self, directions):
        [up, down, left, right] = directions
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.x = 0
        self.y = 0
        self.save_coord()
        self.seen = []
        self.add_seen()

    def parse_coord(self):
        return int_list(self.coord.split(","))

    def save_coord(self):
        self.coord = f"{self.x},{self.y}"

    def save_move(self, d):
        self.move(d)
        self.add_seen()

    def move(self, d):
        [x, y] = self.parse_coord()
        if d == self.up:
            y += 1
        elif d == self.right:
            x += 1
        elif d == self.down:
            y -= 1
        elif d == self.left:
            x -= 1
        self.x = x
        self.y = y

    def add_seen(self):
        self.save_coord()
        if self.coord not in self.seen:
            self.seen.append(self.coord)

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


directions = ["N", "S", "W", "E"]
G = Grid(directions)
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


class S(CacheLayer):

    def is_intersection(self, G):
        G.save_coord()
        return self.p2 == 0 and G.coord in G.seen
    
    def check_intersection(self, G):
        if self.is_intersection(G):
            self.p2 = G.manhattan_distance()

    def solve(self):
        self.split_by_comma()
        self.list_of_tuples()
        direction = directions[0]
        for turn, steps in self.puzzle_input:
            direction = pivot[f'{direction}{turn}']
            while steps > 0:
                G.move(direction)
                self.check_intersection(G)
                G.add_seen()
                steps -= 1
        self.p1 = G.manhattan_distance()
def int_list(a):
    return [int(i) for i in a]


def is_even(i):
    return i % 2 == 0


def combine(a, b):
    return len(a + list(set(b) - set(a)))


def parse_coord(coord):
    return [int(i) for i in coord.split(',')]


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
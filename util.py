def int_list(a):
    return [int(i) for i in a]


def is_even(i):
    return i % 2 == 0


def combine(a, b):
    return len(a + list(set(b) - set(a)))


def manhattan_distance(a, b):
    return abs(a) + abs(b)


class Grid:

    def __init__(self, directions):
        [up, down, left, right] = directions
        self.up = up
        self.down = down
        self.left = left
        self.right = right
        self.x = 0
        self.y = 0
        self.seen = []
        self.add_seen()

    def coord(self):
        return f"{self.x},{self.y}"

    def move(self, d):
        if d == self.up:
            self.y += 1
        elif d == self.right:
            self.x += 1
        elif d == self.down:
            self.y -= 1
        elif d == self.left:
            self.x -= 1

    def save_move(self, d):
        self.move(d)
        self.add_seen()

    def add_seen(self):
        coord = self.coord()
        if coord not in self.seen:
            self.seen.append(coord)
def int_list(data):
    return [int(i) for i in data]


def split_by_comma(data):
    return data.split(', ')


def split_by_new_line(data):
    return data.split('\n')


def list_of_tuples(data):
    return [(d[0], int(d[1:len(d)])) for d in data]


class Grid:

    def __init__(self, directions):
        self.seen = []
        self.x = 0
        self.y = 0
        self.save_coord()
        self.add_seen()
        self.setup_directions(directions)
        
    def setup_directions(self, directions):
        [up, down, left, right] = directions
        self.up = up
        self.down = down
        self.left = left
        self.right = right

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
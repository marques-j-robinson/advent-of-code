from format_data import parse_coord


class Grid:

    def __init__(self, directions, origin='0,0'):
        self.directions = directions
        self.x = 0
        self.y = 0
        self.coord = origin
        self.seen = [origin]

    def move(self, d):
        [x, y] = parse_coord(self.coord)
        if d == self.directions["up"]:
            y += 1
        elif d == self.directions["right"]:
            x += 1
        elif d == self.directions["down"]:
            y -= 1
        elif d == self.directions["left"]:
            x -= 1
        self.x = x
        self.y = y
        self.coord = f"{x},{y}"

    def move_auto(self, d):
        self.move(d)
        self.add_seen()

    def add_seen(self):
        if self.coord not in self.seen:
            self.seen.append(self.coord)